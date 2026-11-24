import os
from pathlib import Path
from typing import List

# Paths to assets and directories
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "Models"

PLANT_MODEL_PATH = MODELS_DIR / "Plant Disease" / "plant-disease-model.pth"
PLANT_CLASSES_PATH = MODELS_DIR / "Plant Disease" / "classes.json"

CROP_MODEL_PATH = MODELS_DIR / "CRS.pkl"
CROP_DATASET_PATH = BASE_DIR / "Datasets" / "Crop_recommendation.csv"

YIELD_MODEL_PATH = MODELS_DIR / "bagging_regressor.pkl"
YIELD_DATASET_PATH = BASE_DIR / "Datasets" / "Crop yeild dataset" / "yield_df.csv"

TEST_IMAGES_DIR = BASE_DIR / "test" / "test"

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'agrivision.db'}")

# Supported CORS origins
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    "*"
]

class Settings:
    PROJECT_NAME: str = "AgriVision AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DESCRIPTION: str = "Intelligent Agriculture and Crop Health Monitoring Decision-Support System"
    
    BASE_DIR: Path = BASE_DIR
    MODELS_DIR: Path = MODELS_DIR
    
    PLANT_MODEL_PATH: Path = PLANT_MODEL_PATH
    PLANT_CLASSES_PATH: Path = PLANT_CLASSES_PATH
    
    CROP_MODEL_PATH: Path = CROP_MODEL_PATH
    CROP_DATASET_PATH: Path = CROP_DATASET_PATH
    
    YIELD_MODEL_PATH: Path = YIELD_MODEL_PATH
    YIELD_DATASET_PATH: Path = YIELD_DATASET_PATH
    
    TEST_IMAGES_DIR: str = str(TEST_IMAGES_DIR)
    DATABASE_URL: str = DATABASE_URL
    CORS_ORIGINS: List[str] = CORS_ORIGINS

settings = Settings()
