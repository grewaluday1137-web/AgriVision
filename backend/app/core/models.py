from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, JSON, Text
from app.core.database import Base

class PredictionRecord(Base):
    __tablename__ = "prediction_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module = Column(String(50), nullable=False, index=True)  # 'disease', 'crop', 'yield'
    input_summary = Column(Text, nullable=False)
    prediction_result = Column(String(255), nullable=False)
    confidence = Column(Float, nullable=True)
    details_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
