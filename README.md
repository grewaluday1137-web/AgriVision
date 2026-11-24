# 🌾 AgriVision AI — Intelligent Agricultural Decision Support Platform

AgriVision AI is an enterprise-grade agricultural decision support platform that combines **Deep Computer Vision**, **Gradient Boosted Decision Trees**, and **Ensemble Regressors** into a unified, high-aesthetic web interface.

---

## 🚀 Quick Start (Single-Command Launch)

To launch both the FastAPI backend and Vite React frontend concurrently:

```powershell
python run.py
```

Once launched:
- **Web Application**: [http://localhost:5173](http://localhost:5173)
- **Interactive Swagger API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **System Health & Hardware Acceleration**: [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

## 🧠 System Architecture & Machine Learning Modules

| Module | Core Algorithm / Framework | Training Data & Scope | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **Plant Doctor** | **ResNet9 Deep CNN** (PyTorch) | 87,000+ Leaf Images (PlantVillage) | Detects **38 plant pathologies** and healthy states. Provides Top-3 probability breakdown and curated organic/chemical treatment prescriptions. Includes a **1-click test specimen carousel** (33 leaves). |
| **Crop Advisor** | **XGBoost Classifier** | Soil & Climate Dataset (2,200 records) | Recommends optimal crops across **22 varieties** based on Soil Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall. Features **5 regional biome presets**. |
| **Yield Forecaster** | **Bagging Regressor Ensemble** | FAOSTAT Global Yield Records | Projects harvest yields across **101 countries** and **10 staple crops** based on precipitation, pesticides, and temperature. Provides conversion to metric tonnes/ha and regional baseline benchmarks. |
| **Agronomic Encyclopedia** | **Curated Knowledge Engine** | 38 Curated Pathology Records | Comprehensive library of symptoms, biological controls, chemical fungicides, and preventive cultural practices. Searchable and filterable by crop. |
| **Audit History** | **SQLAlchemy + SQLite / PostgreSQL** | Persistent Ingestion Records | Real-time audit log of all predictions with timestamp, input parameters, model confidence, and JSON export. |

---

## 🎨 Frontend Features & Design System
- **Framework**: React 19 + Vite 6 + Tailwind CSS v4 + Lucide Icons.
- **Theme**: Agricultural color palette (Emerald green `#059669`, Mint `#10B981`, Harvest gold `#D97706`) with glassmorphic cards and subtle animations.
- **Theme Modes**: Native **Dark / Light Mode Toggle** with state saved to `localStorage`.
- **Hardware Badge**: Real-time indicator detecting GPU acceleration (e.g. `NVIDIA GeForce RTX 3050 6GB Laptop GPU` via CUDA 12.6).

---

## 🧪 Verification & Testing

To execute automated end-to-end integration tests:

```powershell
cd backend
python test_e2e.py
```

All 6 validation checkpoints (System Health, Plant Doctor, Crop Advisor, Yield Forecaster, Encyclopedia, and History Logging) are tested automatically.
