from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.core.schemas import DiseaseGuidance
from app.knowledge.disease_guidance import get_disease_guidance, list_all_guidance

router = APIRouter(prefix="/guidance", tags=["Agronomic Encyclopedia"])

@router.get("", response_model=List[DiseaseGuidance])
def list_guidance(
    crop: Optional[str] = Query(None, description="Filter by crop name (e.g., Apple, Tomato, Corn)"),
    search: Optional[str] = Query(None, description="Search term in disease name, symptoms, or remedies")
):
    """
    Retrieves the comprehensive agronomic database of 38 plant disease classes,
    complete with symptom descriptions, biological cures, chemical treatments, and prevention measures.
    """
    all_items = list_all_guidance()
    
    if crop:
        crop_clean = crop.strip().lower()
        all_items = [item for item in all_items if item["crop"].lower() == crop_clean]
        
    if search:
        s = search.strip().lower()
        all_items = [
            item for item in all_items
            if s in item["disease"].lower()
            or s in item["crop"].lower()
            or s in item["summary"].lower()
            or any(s in sym.lower() for sym in item["symptoms"])
            or any(s in org.lower() for org in item["organic_treatments"])
        ]
        
    return [DiseaseGuidance(**item) for item in all_items]


@router.get("/{disease_key}", response_model=DiseaseGuidance)
def get_guidance_by_key(disease_key: str):
    """
    Fetch specific agronomic treatment and symptom guidance for a plant disease key.
    """
    guidance = get_disease_guidance(disease_key)
    if not guidance:
        raise HTTPException(status_code=404, detail=f"No guidance found for disease identifier '{disease_key}'.")
    return DiseaseGuidance(**guidance)
