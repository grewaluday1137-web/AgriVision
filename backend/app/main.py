import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.core.database import init_db
from app.adapters.disease_adapter import disease_adapter
from app.adapters.crop_adapter import crop_adapter
from app.adapters.yield_adapter import yield_adapter

# Import API Routers
from app.api.endpoints.health import router as health_router
from app.api.endpoints.disease import router as disease_router
from app.api.endpoints.crop import router as crop_router
from app.api.endpoints.yield_module import router as yield_router
from app.api.endpoints.guidance import router as guidance_router
from app.api.endpoints.history import router as history_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle manager.
    Initializes database tables and pre-warms all 3 machine learning models.
    """
    print("\n" + "=" * 60)
    print("🌾 AgriVision AI Backend Initializing...")
    print("=" * 60)
    
    # 1. Initialize SQLite / Postgres tables
    init_db()
    print("✅ Database initialized successfully.")
    
    # 2. Preload Plant Disease ResNet9 model
    disease_adapter.load_model()
    print(f"✅ Disease Classifier ready on {disease_adapter.device}.")
    
    # 3. Preload Crop Recommendation XGBoost model
    crop_adapter.load_model()
    print(f"✅ Crop Recommender ready ({len(crop_adapter.classes_)} crops supported).")
    
    # 4. Preload Harvest Yield Bagging Regressor model
    yield_adapter.load_model()
    print(f"✅ Yield Forecaster ready ({len(yield_adapter.country_encoder.classes_)} countries, {len(yield_adapter.crop_encoder.classes_)} crops).")
    
    print("=" * 60)
    print(f"🚀 AgriVision AI API Server Running at: http://localhost:8000")
    print(f"📖 Interactive Docs (Swagger): http://localhost:8000/docs")
    print("=" * 60 + "\n")
    
    yield
    
    print("\n🛑 AgriVision AI Server shutting down cleanly.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Unified Enterprise-Grade Agricultural Intelligence Platform with Leaf Disease Diagnosis, Crop Recommendation, and Yield Forecasting.",
    lifespan=lifespan
)

# CORS Configuration for local Vite and external evaluators
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers under /api
app.include_router(health_router, prefix=settings.API_PREFIX)
app.include_router(disease_router, prefix=settings.API_PREFIX)
app.include_router(crop_router, prefix=settings.API_PREFIX)
app.include_router(yield_router, prefix=settings.API_PREFIX)
app.include_router(guidance_router, prefix=settings.API_PREFIX)
app.include_router(history_router, prefix=settings.API_PREFIX)

@app.get("/", tags=["Root"])
def root_status():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs_url": "/docs",
        "health_check": f"{settings.API_PREFIX}/health",
        "modules": {
            "plant_doctor": f"{settings.API_PREFIX}/disease",
            "crop_advisor": f"{settings.API_PREFIX}/crop",
            "yield_forecaster": f"{settings.API_PREFIX}/yield",
            "encyclopedia": f"{settings.API_PREFIX}/guidance",
            "history": f"{settings.API_PREFIX}/history"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
