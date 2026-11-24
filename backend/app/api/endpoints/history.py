from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.models import PredictionRecord
from app.core.schemas import HistoryItemResponse
from app.api.deps import get_db_session

router = APIRouter(prefix="/history", tags=["Prediction History"])

@router.get("", response_model=List[HistoryItemResponse])
def get_history(
    module: Optional[str] = Query(None, description="Filter by module: 'disease', 'crop', or 'yield'"),
    limit: int = Query(50, ge=1, le=200, description="Maximum records to return"),
    db: Session = Depends(get_db_session)
):
    """
    Fetch prediction history records stored during Plant Doctor, Crop Advisor, or Yield Forecaster sessions.
    """
    query = db.query(PredictionRecord)
    if module:
        query = query.filter(PredictionRecord.module == module.strip().lower())
    
    records = query.order_by(desc(PredictionRecord.created_at)).limit(limit).all()
    
    return [
        HistoryItemResponse(
            id=rec.id,
            module=rec.module,
            created_at=rec.created_at.isoformat(),
            input_summary=rec.input_summary,
            prediction_result=rec.prediction_result,
            confidence=rec.confidence,
            details=rec.details_json or {}
        )
        for rec in records
    ]


@router.delete("/{record_id}")
def delete_history_item(
    record_id: int,
    db: Session = Depends(get_db_session)
):
    """
    Delete a specific prediction history record.
    """
    record = db.query(PredictionRecord).filter(PredictionRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail=f"History record with ID {record_id} not found.")
    
    db.delete(record)
    db.commit()
    return {"status": "success", "message": f"Record {record_id} deleted."}


@router.delete("")
def clear_all_history(
    module: Optional[str] = Query(None, description="Clear history only for a specific module"),
    db: Session = Depends(get_db_session)
):
    """
    Clear all prediction history records (optionally filtered by module).
    """
    query = db.query(PredictionRecord)
    if module:
        query = query.filter(PredictionRecord.module == module.strip().lower())
        
    deleted_count = query.delete(synchronize_session=False)
    db.commit()
    return {"status": "success", "message": f"Cleared {deleted_count} history records."}
