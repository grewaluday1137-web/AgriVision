from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.schemas import YieldPredictionRequest, YieldPredictionResponse, YieldManifestResponse
from app.adapters.yield_adapter import yield_adapter
from app.core.models import PredictionRecord
from app.api.deps import get_db_session

router = APIRouter(prefix="/yield", tags=["Yield Forecaster"])

@router.post("/predict", response_model=YieldPredictionResponse)
def predict_yield(
    req: YieldPredictionRequest,
    db: Session = Depends(get_db_session)
):
    """
    Predicts agricultural crop harvest yield using the Bagging Regressor trained on FAO datasets,
    taking country, crop, year, rainfall, pesticide usage, and average temperature.
    Provides conversions to hectograms/ha, tonnes/ha, and kg/ha with regional benchmarks.
    """
    try:
        result = yield_adapter.predict(
            country=req.country,
            crop=req.crop,
            year=req.year,
            rainfall_mm=req.rainfall_mm,
            pesticides_tonnes=req.pesticides_tonnes,
            avg_temp_celsius=req.avg_temp_celsius
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Save record to database
    try:
        summary_str = f"{req.crop} in {req.country} ({req.year}) | Rain:{req.rainfall_mm}mm Temp:{req.avg_temp_celsius}°C"
        rec = PredictionRecord(
            module="yield",
            input_summary=summary_str,
            prediction_result=f"{result['predicted_yield_tonnes_per_hectare']} tonnes/ha ({result['predicted_yield_hg_per_ha']:,.0f} hg/ha)",
            confidence=0.92,  # R2 score of the bagging regressor on FAO test set
            details_json={
                "inputs": req.model_dump(),
                "predictions": result
            }
        )
        db.add(rec)
        db.commit()
    except Exception as db_err:
        print(f"[Warning] Failed to record yield history: {db_err}")
        
    return YieldPredictionResponse(**result)


@router.get("/manifest", response_model=YieldManifestResponse)
def get_yield_manifest():
    """
    Returns the supported countries (101), crops (10), realistic feature boundaries,
    and unit metadata to dynamically populate frontend controls.
    """
    return YieldManifestResponse(**yield_adapter.get_manifest())
