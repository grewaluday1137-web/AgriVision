import io
import json
import logging
from typing import List, Dict, Tuple, Any, Optional
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms

from app.core.config import PLANT_MODEL_PATH, PLANT_CLASSES_PATH

logger = logging.getLogger(__name__)

def ConvBlock(in_channels: int, out_channels: int, pool: bool = False):
    layers = [
        nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(inplace=True)
    ]
    if pool:
        layers.append(nn.MaxPool2d(4))
    return nn.Sequential(*layers)

class ResNet9(nn.Module):
    def __init__(self, in_channels: int, num_classes: int):
        super().__init__()
        self.conv1 = ConvBlock(in_channels, 64)
        self.conv2 = ConvBlock(64, 128, pool=True)
        self.res1 = nn.Sequential(ConvBlock(128, 128), ConvBlock(128, 128))

        self.conv3 = ConvBlock(128, 256, pool=True)
        self.conv4 = ConvBlock(256, 512, pool=True)
        self.res2 = nn.Sequential(ConvBlock(512, 512), ConvBlock(512, 512))

        self.classifier = nn.Sequential(
            nn.MaxPool2d(4),
            nn.Flatten(),
            nn.Linear(512, num_classes)
        )

    def forward(self, xb):
        out = self.conv1(xb)
        out = self.conv2(out)
        out = self.res1(out) + out
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.res2(out) + out
        out = self.classifier(out)
        return out

class PlantDiseaseAdapter:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.classes: List[str] = []
        self.model: Optional[ResNet9] = None
        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor()
        ])
        self.load_model()

    def is_loaded(self) -> bool:
        return self.model is not None and len(self.classes) > 0

    def load_model(self):
        try:
            with open(PLANT_CLASSES_PATH, "r", encoding="utf-8") as f:
                self.classes = json.load(f)
            
            self.model = ResNet9(3, len(self.classes))
            state_dict = torch.load(PLANT_MODEL_PATH, map_location=self.device)
            self.model.load_state_dict(state_dict)
            self.model.to(self.device)
            self.model.eval()
            logger.info(f"Plant Disease ResNet9 model loaded on {self.device} ({len(self.classes)} classes).")
        except Exception as e:
            logger.error(f"Failed to load Plant Disease model: {e}")
            raise e

    @staticmethod
    def format_label(raw_class: str) -> Tuple[str, str, bool]:
        parts = raw_class.split("___")
        crop = parts[0].replace("_", " ").title()
        if len(parts) > 1:
            disease = parts[1].replace("_", " ").title()
        else:
            disease = "Healthy"
        
        is_healthy = "healthy" in raw_class.lower()
        if is_healthy:
            disease = "Healthy Condition"
            
        return crop, disease, is_healthy

    def predict_image_bytes(self, image_bytes: bytes) -> Dict[str, Any]:
        if self.model is None:
            raise RuntimeError("Plant disease model is not loaded.")

        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(tensor)
            probs = torch.softmax(outputs, dim=1)[0]
            top_k_probs, top_k_indices = torch.topk(probs, k=min(3, len(self.classes)))

        top_pred_idx = top_k_indices[0].item()
        top_pred_class = self.classes[top_pred_idx]
        top_confidence = float(top_k_probs[0].item())

        crop, disease, is_healthy = self.format_label(top_pred_class)

        top_predictions = []
        for prob, idx in zip(top_k_probs, top_k_indices):
            cls_name = self.classes[idx.item()]
            c_name, d_name, _ = self.format_label(cls_name)
            p_val = float(prob.item())
            top_predictions.append({
                "class_name": cls_name,
                "crop": c_name,
                "disease": d_name,
                "confidence": round(p_val, 4),
                "confidence_pct": round(p_val * 100, 2)
            })

        return {
            "crop": crop,
            "disease": disease,
            "raw_class_name": top_pred_class,
            "confidence": round(top_confidence, 4),
            "confidence_pct": round(top_confidence * 100, 2),
            "is_healthy": is_healthy,
            "top_predictions": top_predictions
        }

    def predict_image_path(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, "rb") as f:
            return self.predict_image_bytes(f.read())

    def predict(self, image_bytes: bytes) -> Dict[str, Any]:
        return self.predict_image_bytes(image_bytes)

disease_adapter = PlantDiseaseAdapter()
