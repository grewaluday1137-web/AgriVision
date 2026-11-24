from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.schemas import CropRecommendationRequest, CropRecommendationResponse
from app.adapters.crop_adapter import crop_adapter
from app.core.models import PredictionRecord
from app.api.deps import get_db_session

router = APIRouter(prefix="/crop", tags=["Crop Advisor"])

@router.post("/recommend", response_model=CropRecommendationResponse)
def recommend_crop(
    req: CropRecommendationRequest,
    db: Session = Depends(get_db_session)
):
    """
    Evaluates soil N-P-K nutrient composition and ambient climatic parameters (temperature,
    humidity, pH, rainfall) using the trained XGBoost Classifier to recommend the optimal crop.
    """
    try:
        result = crop_adapter.predict(
            nitrogen=req.nitrogen,
            phosphorus=req.phosphorus,
            potassium=req.potassium,
            temperature=req.temperature,
            humidity=req.humidity,
            ph=req.ph,
            rainfall=req.rainfall
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Crop recommendation failure: {str(e)}")
    
    # Save record to database
    try:
        summary_str = f"N:{req.nitrogen} P:{req.phosphorus} K:{req.potassium} | Temp:{req.temperature}°C Rain:{req.rainfall}mm"
        rec = PredictionRecord(
            module="crop",
            input_summary=summary_str,
            prediction_result=f"{result['recommended_crop']} ({result['confidence_pct']}%)",
            confidence=result["confidence"],
            details_json={
                "inputs": req.model_dump(),
                "recommended_crop": result["recommended_crop"],
                "raw_crop_name": result["raw_crop_name"],
                "confidence": result["confidence"],
                "top_alternatives": result["top_alternatives"],
                "soil_suitability_analysis": result["soil_suitability_analysis"]
            }
        )
        db.add(rec)
        db.commit()
    except Exception as db_err:
        print(f"[Warning] Failed to record crop history: {db_err}")
        
    return CropRecommendationResponse(**result)


@router.get("/presets", response_model=List[Dict[str, Any]])
def get_crop_presets():
    """
    Returns realistic agricultural environmental presets representing diverse biomes
    and soil conditions for rapid 1-click evaluation.
    """
    return [
        {
            "id": "monsoon_wetland",
            "name": "Tropical Monsoon Wetland",
            "description": "High rainfall, high humidity, warm tropical climate ideal for paddy and wetland crops.",
            "data": {
                "nitrogen": 90.0,
                "phosphorus": 42.0,
                "potassium": 43.0,
                "temperature": 23.5,
                "humidity": 82.0,
                "ph": 6.5,
                "rainfall": 202.9
            }
        },
        {
            "id": "arid_dryland",
            "name": "Semi-Arid Dryland & Pulses",
            "description": "Moderate temperature, low rainfall, slightly alkaline soil suitable for hardy drought-resistant crops.",
            "data": {
                "nitrogen": 22.0,
                "phosphorus": 68.0,
                "potassium": 21.0,
                "temperature": 27.5,
                "humidity": 45.0,
                "ph": 7.3,
                "rainfall": 65.0
            }
        },
        {
            "id": "black_cotton_fertile",
            "name": "Fertile Black Cotton Soil",
            "description": "High potassium, moderate nitrogen, balanced pH, warm sub-tropical conditions.",
            "data": {
                "nitrogen": 115.0,
                "phosphorus": 40.0,
                "potassium": 20.0,
                "temperature": 25.8,
                "humidity": 80.0,
                "ph": 6.8,
                "rainfall": 70.0
            }
        },
        {
            "id": "temperate_highland",
            "name": "Temperate Highland Orchard",
            "description": "Cooler temperatures, moderate rainfall, slightly acidic loamy soil.",
            "data": {
                "nitrogen": 20.0,
                "phosphorus": 134.0,
                "potassium": 198.0,
                "temperature": 22.0,
                "humidity": 92.0,
                "ph": 5.9,
                "rainfall": 112.0
            }
        },
        {
            "id": "coastal_sandy_loam",
            "name": "Coastal Sandy Loam",
            "description": "High humidity, warm year-round temperature, and abundant rainfall.",
            "data": {
                "nitrogen": 18.0,
                "phosphorus": 30.0,
                "potassium": 30.0,
                "temperature": 27.0,
                "humidity": 95.0,
                "ph": 6.2,
                "rainfall": 175.0
            }
        }
    ]
