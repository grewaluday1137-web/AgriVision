import pickle
import logging
import warnings
import numpy as np
import pandas as pd
from typing import Dict, Any, List
from sklearn.preprocessing import LabelEncoder

from app.core.config import CROP_MODEL_PATH, CROP_DATASET_PATH

logger = logging.getLogger(__name__)

class CropRecommendationAdapter:
    def __init__(self):
        self.model = None
        self.label_encoder = LabelEncoder()
        self.feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        self.dataset_stats: Dict[str, Dict[str, float]] = {}
        self.load_model()

    @property
    def classes_(self):
        return self.label_encoder.classes_

    def is_loaded(self) -> bool:
        return self.model is not None and len(self.label_encoder.classes_) > 0

    def load_model(self):
        try:
            df = pd.read_csv(CROP_DATASET_PATH)
            self.label_encoder.fit(df['label'])

            for col in self.feature_names:
                self.dataset_stats[col] = {
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "mean": float(df[col].mean()),
                    "median": float(df[col].median()),
                }

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                with open(CROP_MODEL_PATH, "rb") as f:
                    self.model = pickle.load(f)

            logger.info(f"Crop Recommendation model loaded ({len(self.label_encoder.classes_)} crops).")
        except Exception as e:
            logger.error(f"Failed to load Crop Recommendation model: {e}")
            raise e

    def predict(
        self,
        nitrogen: float = 0.0,
        phosphorus: float = 0.0,
        potassium: float = 0.0,
        temperature: float = 0.0,
        humidity: float = 0.0,
        ph: float = 7.0,
        rainfall: float = 0.0,
        **kwargs
    ) -> Dict[str, Any]:
        if self.model is None:
            raise RuntimeError("Crop Recommendation model is not loaded.")

        # Support alias keywords (n, p, k, temp)
        n = kwargs.get('n', nitrogen)
        p = kwargs.get('p', phosphorus)
        k = kwargs.get('k', potassium)
        temp = kwargs.get('temp', temperature)

        input_data = pd.DataFrame([{
            'N': float(n),
            'P': float(p),
            'K': float(k),
            'temperature': float(temp),
            'humidity': float(humidity),
            'ph': float(ph),
            'rainfall': float(rainfall)
        }], columns=self.feature_names)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            predicted_encoded = self.model.predict(input_data)[0]
            probabilities = self.model.predict_proba(input_data)[0]

        raw_crop_name = self.label_encoder.inverse_transform([predicted_encoded])[0]
        recommended_crop = raw_crop_name.replace("_", " ").title()
        top_confidence = float(probabilities[predicted_encoded])

        sorted_indices = np.argsort(probabilities)[::-1]
        top_alternatives: List[Dict[str, Any]] = []
        for idx in sorted_indices[:4]:
            alt_raw = self.label_encoder.inverse_transform([idx])[0]
            alt_title = alt_raw.replace("_", " ").title()
            prob = float(probabilities[idx])
            top_alternatives.append({
                "crop": alt_title,
                "raw_crop_name": alt_raw,
                "confidence": round(prob, 4),
                "confidence_pct": round(prob * 100, 2)
            })

        # Soil & Climatic Factors Analysis
        favorable_factors = []
        limiting_factors = []

        if 6.0 <= ph <= 7.5:
            favorable_factors.append(f"Soil pH ({ph:.1f}) is neutral and optimal for nutrient absorption.")
        elif ph < 6.0:
            limiting_factors.append(f"Soil pH ({ph:.1f}) is acidic; consider agricultural lime.")
        else:
            limiting_factors.append(f"Soil pH ({ph:.1f}) is alkaline; consider organic matter or gypsum.")

        if rainfall >= 150:
            favorable_factors.append(f"Abundant rainfall ({rainfall:.0f} mm) sustains water-intensive cultivation.")
        elif rainfall < 75:
            limiting_factors.append(f"Low rainfall ({rainfall:.0f} mm); supplemental irrigation or drip systems suggested.")
        else:
            favorable_factors.append(f"Moderate precipitation ({rainfall:.0f} mm) provides balanced hydration.")

        if n >= 70:
            favorable_factors.append(f"Rich nitrogen levels ({n:.0f} kg/ha) provide robust vegetative canopy growth.")
        elif n < 35:
            limiting_factors.append(f"Low nitrogen ({n:.0f} kg/ha); consider compost or urea top-dressing.")

        if temp > 35:
            limiting_factors.append(f"High ambient heat ({temp:.1f}°C) may require heat-tolerant cultivars.")
        elif temp < 15:
            limiting_factors.append(f"Cool temperatures ({temp:.1f}°C) may slow germination.")

        soil_analysis = {
            "nitrogen_status": "High" if n > 80 else ("Low" if n < 40 else "Optimal"),
            "phosphorus_status": "High" if p > 70 else ("Low" if p < 30 else "Optimal"),
            "potassium_status": "High" if k > 80 else ("Low" if k < 30 else "Optimal"),
            "ph_category": "Acidic" if ph < 6.0 else ("Alkaline" if ph > 7.5 else "Optimal"),
            "favorable_factors": favorable_factors,
            "limiting_factors": limiting_factors
        }

        return {
            "recommended_crop": recommended_crop,
            "raw_crop_name": raw_crop_name,
            "confidence": round(top_confidence, 4),
            "confidence_pct": round(top_confidence * 100, 2),
            "top_alternatives": top_alternatives,
            "soil_suitability_analysis": soil_analysis
        }

crop_adapter = CropRecommendationAdapter()
