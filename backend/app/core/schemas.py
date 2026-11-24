from typing import Generic, TypeVar, Optional, List, Any, Dict
from pydantic import BaseModel, Field
from datetime import datetime

T = TypeVar("T")

class BaseEnvelope(BaseModel, Generic[T]):
    request_id: str
    module: str
    status: str = "success"
    result: Optional[T] = None
    model_version: str = "v1.0.0"
    warnings: List[str] = Field(default_factory=list)
    generated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

# ==================== Health Schemas ====================
class HealthResponse(BaseModel):
    status: str
    version: str
    device: str
    models_loaded: Dict[str, bool]
    system_metrics: Dict[str, Any]

# ==================== Disease Schemas ====================
class DiseaseCandidate(BaseModel):
    class_name: str
    crop: str
    disease: str
    confidence: float
    confidence_pct: float

class DiseaseGuidance(BaseModel):
    disease_key: str
    crop: str
    disease: str
    is_healthy: bool
    summary: str
    symptoms: List[str]
    organic_treatments: List[str]
    chemical_treatments: List[str]
    prevention_methods: List[str]

class DiseasePredictionResponse(BaseModel):
    crop: str
    disease: str
    raw_class_name: str
    confidence: float
    confidence_pct: float
    is_healthy: bool
    top_predictions: List[Dict[str, Any]]
    guidance: Optional[Dict[str, Any]] = None

class SampleImageInfo(BaseModel):
    filename: str
    display_name: str
    image_url: str
    predicted_class_hint: str

# ==================== Crop Recommendation Schemas ====================
class CropRecommendationRequest(BaseModel):
    nitrogen: float = Field(..., ge=0, le=200, description="Nitrogen content in soil (kg/ha)")
    phosphorus: float = Field(..., ge=0, le=200, description="Phosphorus content in soil (kg/ha)")
    potassium: float = Field(..., ge=0, le=250, description="Potassium content in soil (kg/ha)")
    temperature: float = Field(..., ge=0, le=60, description="Environmental temperature in °C")
    humidity: float = Field(..., ge=0, le=100, description="Relative humidity in %")
    ph: float = Field(..., ge=2, le=12, description="Soil pH level (2.0 - 12.0)")
    rainfall: float = Field(..., ge=0, le=500, description="Annual rainfall in mm")

class CropRecommendationResponse(BaseModel):
    recommended_crop: str
    raw_crop_name: str
    confidence: float
    confidence_pct: float
    top_alternatives: List[Dict[str, Any]]
    soil_suitability_analysis: Dict[str, Any]

# ==================== Yield Prediction Schemas ====================
class YieldPredictionRequest(BaseModel):
    country: str = Field(..., description="Country name from supported manifest")
    crop: str = Field(..., description="Crop name from supported manifest")
    year: int = Field(default=2024, ge=1990, le=2030, description="Harvest year")
    rainfall_mm: float = Field(..., ge=10, le=5000, description="Average rainfall in mm/year")
    pesticides_tonnes: float = Field(..., ge=0, le=500000, description="Pesticide usage in tonnes")
    avg_temp_celsius: float = Field(..., ge=-10, le=50, description="Average temperature in °C")

class YieldPredictionResponse(BaseModel):
    country: str
    crop: str
    year: int
    predicted_yield_hg_per_ha: float
    predicted_yield_tonnes_per_hectare: float
    predicted_yield_kg_per_ha: float
    historical_benchmark_hg_ha: Optional[float] = None
    performance_band: str
    context_notes: str

class YieldManifestResponse(BaseModel):
    supported_countries: List[str]
    supported_crops: List[str]
    year_range: Dict[str, int]
    rainfall_range_mm: Dict[str, float]
    pesticides_range_tonnes: Dict[str, float]
    temp_range_celsius: Dict[str, float]
    unit_explanations: Dict[str, str]

# ==================== History Schemas ====================
class HistoryItemResponse(BaseModel):
    id: int
    module: str
    created_at: str
    input_summary: str
    prediction_result: str
    confidence: Optional[float] = None
    details: Dict[str, Any]
