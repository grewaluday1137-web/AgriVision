import torch
import psutil
from fastapi import APIRouter
from app.core.schemas import HealthResponse
from app.adapters.disease_adapter import disease_adapter
from app.adapters.crop_adapter import crop_adapter
from app.adapters.yield_adapter import yield_adapter

router = APIRouter(prefix="/health", tags=["System Health"])

@router.get("", response_model=HealthResponse)
def get_health() -> HealthResponse:
    """Return system status, hardware acceleration information, and model states."""
    models_status = {
        "plant_disease_resnet9": disease_adapter.is_loaded(),
        "crop_recommender_xgboost": crop_adapter.is_loaded(),
        "yield_predictor_bagging": yield_adapter.is_loaded()
    }
    
    cuda_available = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_available else "CPU (Host)"
    
    system_metrics = {
        "cpu_percent": psutil.cpu_percent(),
        "virtual_memory_percent": psutil.virtual_memory().percent,
        "cuda_available": cuda_available,
        "device_name": device_name,
        "torch_version": torch.__version__
    }
    
    if cuda_available:
        try:
            allocated = torch.cuda.memory_allocated(0) / (1024 ** 2)
            reserved = torch.cuda.memory_reserved(0) / (1024 ** 2)
            system_metrics["gpu_memory_allocated_mb"] = round(allocated, 2)
            system_metrics["gpu_memory_reserved_mb"] = round(reserved, 2)
        except Exception:
            pass

    all_models_healthy = all(models_status.values())
    status_str = "healthy" if all_models_healthy else "degraded"

    return HealthResponse(
        status=status_str,
        version="1.0.0",
        device=device_name,
        models_loaded=models_status,
        system_metrics=system_metrics
    )
