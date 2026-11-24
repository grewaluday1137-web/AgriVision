import os
import shutil
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.schemas import DiseasePredictionResponse, SampleImageInfo
from app.adapters.disease_adapter import disease_adapter
from app.knowledge.disease_guidance import get_disease_guidance
from app.core.models import PredictionRecord
from app.api.deps import get_db_session

router = APIRouter(prefix="/disease", tags=["Plant Doctor"])

@router.post("/predict", response_model=DiseasePredictionResponse)
async def predict_disease(
    file: UploadFile = File(...),
    notes: Optional[str] = Form(None),
    db: Session = Depends(get_db_session)
):
    """
    Accepts an uploaded plant leaf image, passes it to the ResNet9 PyTorch classifier,
    retrieves agronomic treatment guidance, and records the prediction in history.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image (JPEG, PNG, WebP).")
    
    # Read image bytes
    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")
    
    try:
        raw_pred = disease_adapter.predict_image_bytes(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
    
    # Retrieve guidance from curated agronomic knowledge base
    guidance = get_disease_guidance(raw_pred["raw_class_name"])
    
    # Save record to database
    try:
        rec = PredictionRecord(
            module="disease",
            input_summary=f"Leaf image: {file.filename} ({len(contents)//1024} KB)",
            prediction_result=f"{raw_pred['crop']} - {raw_pred['disease']} ({raw_pred['confidence_pct']}%)",
            confidence=raw_pred["confidence"],
            details_json={
                "filename": file.filename,
                "crop": raw_pred["crop"],
                "disease": raw_pred["disease"],
                "is_healthy": raw_pred["is_healthy"],
                "confidence": raw_pred["confidence"],
                "top_predictions": raw_pred["top_predictions"],
                "guidance_summary": guidance["summary"] if guidance else None,
                "user_notes": notes
            }
        )
        db.add(rec)
        db.commit()
    except Exception as db_err:
        # Non-fatal DB logging failure
        print(f"[Warning] Failed to record history in DB: {db_err}")
    
    return DiseasePredictionResponse(
        crop=raw_pred["crop"],
        disease=raw_pred["disease"],
        raw_class_name=raw_pred["raw_class_name"],
        confidence=raw_pred["confidence"],
        confidence_pct=raw_pred["confidence_pct"],
        is_healthy=raw_pred["is_healthy"],
        top_predictions=raw_pred["top_predictions"],
        guidance=guidance
    )


@router.post("/predict-sample", response_model=DiseasePredictionResponse)
def predict_sample_image(
    filename: str = Form(...),
    notes: Optional[str] = Form(None),
    db: Session = Depends(get_db_session)
):
    """
    Run 1-click inference on an existing sample image from the test/test directory.
    """
    file_path = os.path.join(settings.TEST_IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Sample image '{filename}' not found.")
    
    try:
        raw_pred = disease_adapter.predict_image_path(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
    
    guidance = get_disease_guidance(raw_pred["raw_class_name"])
    
    # Save record to database
    try:
        rec = PredictionRecord(
            module="disease",
            input_summary=f"Sample leaf: {filename}",
            prediction_result=f"{raw_pred['crop']} - {raw_pred['disease']} ({raw_pred['confidence_pct']}%)",
            confidence=raw_pred["confidence"],
            details_json={
                "filename": filename,
                "crop": raw_pred["crop"],
                "disease": raw_pred["disease"],
                "is_healthy": raw_pred["is_healthy"],
                "confidence": raw_pred["confidence"],
                "top_predictions": raw_pred["top_predictions"],
                "guidance_summary": guidance["summary"] if guidance else None,
                "user_notes": notes,
                "is_sample": True
            }
        )
        db.add(rec)
        db.commit()
    except Exception as db_err:
        print(f"[Warning] Failed to record history in DB: {db_err}")
    
    return DiseasePredictionResponse(
        crop=raw_pred["crop"],
        disease=raw_pred["disease"],
        raw_class_name=raw_pred["raw_class_name"],
        confidence=raw_pred["confidence"],
        confidence_pct=raw_pred["confidence_pct"],
        is_healthy=raw_pred["is_healthy"],
        top_predictions=raw_pred["top_predictions"],
        guidance=guidance
    )


@router.get("/samples", response_model=List[SampleImageInfo])
def list_sample_images():
    """
    Returns curated sample images from the test/test directory for 1-click UI testing.
    """
    samples_dir = settings.TEST_IMAGES_DIR
    if not os.path.exists(samples_dir):
        return []
    
    files = sorted(os.listdir(samples_dir))
    results = []
    
    # Map common prefixes to human friendly hints
    for fname in files:
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        
        # Clean label hint from filename
        hint = fname.replace(".JPG", "").replace(".jpg", "").replace(".png", "")
        # Add spaces before capital letters for readability
        formatted_hint = "".join([" " + c if c.isupper() and i > 0 and not fname[i-1].isupper() else c for i, c in enumerate(hint)]).strip()
        
        results.append(SampleImageInfo(
            filename=fname,
            display_name=formatted_hint,
            image_url=f"/api/disease/sample-image/{fname}",
            predicted_class_hint=hint
        ))
    
    return results


@router.get("/sample-image/{filename}")
def get_sample_image(filename: str):
    """
    Serves a sample image file directly so the frontend can preview and display it.
    """
    file_path = os.path.join(settings.TEST_IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Sample image not found.")
    
    media_type = "image/jpeg"
    if filename.lower().endswith(".png"):
        media_type = "image/png"
    elif filename.lower().endswith(".webp"):
        media_type = "image/webp"
        
    return FileResponse(file_path, media_type=media_type)
