import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from fastapi.testclient import TestClient
from app.main import app
from app.core.database import init_db

init_db()

def test_all():
    with TestClient(app) as client:
        print(">>> 1. Testing Root Endpoint GET /")
        res = client.get("/")
        assert res.status_code == 200, f"Root failed: {res.text}"
        print("Root response:", res.json()["name"])

        print("\n>>> 2. Testing Health GET /api/health")
        res = client.get("/api/health")
        assert res.status_code == 200, f"Health failed: {res.text}"
        health_data = res.json()
        print("Health Status:", health_data["status"], "| Device:", health_data["device"])
        print("Models Loaded:", health_data["models_loaded"])
        assert all(health_data["models_loaded"].values()), "Not all models loaded!"

        print("\n>>> 3. Testing Crop Presets GET /api/crop/presets")
        res = client.get("/api/crop/presets")
        assert res.status_code == 200
        presets = res.json()
        print(f"Loaded {len(presets)} presets. Example: {presets[0]['name']}")

        print("\n>>> 4. Testing Crop Recommend POST /api/crop/recommend")
        crop_payload = {
            "nitrogen": 90,
            "phosphorus": 42,
            "potassium": 43,
            "temperature": 23.5,
            "humidity": 82.0,
            "ph": 6.5,
            "rainfall": 202.9
        }
        res = client.post("/api/crop/recommend", json=crop_payload)
        assert res.status_code == 200, f"Crop recommend failed: {res.text}"
        crop_res = res.json()
        print(f"Recommended Crop: {crop_res['recommended_crop']} (Confidence: {crop_res['confidence_pct']}%)")
        print(f"Top alternatives: {crop_res['top_alternatives']}")

        print("\n>>> 5. Testing Yield Manifest GET /api/yield/manifest")
        res = client.get("/api/yield/manifest")
        assert res.status_code == 200
        manifest = res.json()
        print(f"Countries count: {len(manifest['supported_countries'])}, Crops count: {len(manifest['supported_crops'])}")

        print("\n>>> 6. Testing Yield Predict POST /api/yield/predict")
        yield_payload = {
            "country": "India",
            "crop": "Potatoes",
            "year": 2013,
            "rainfall_mm": 1083.0,
            "pesticides_tonnes": 50000.0,
            "avg_temp_celsius": 26.5
        }
        res = client.post("/api/yield/predict", json=yield_payload)
        assert res.status_code == 200, f"Yield predict failed: {res.text}"
        yield_res = res.json()
        print(f"Yield: {yield_res['predicted_yield_tonnes_per_hectare']} tonnes/ha ({yield_res['predicted_yield_hg_per_ha']} hg/ha)")

        print("\n>>> 7. Testing Disease Samples GET /api/disease/samples")
        res = client.get("/api/disease/samples")
        assert res.status_code == 200
        samples = res.json()
        print(f"Available test samples: {len(samples)}")
        assert len(samples) > 0

        print("\n>>> 8. Testing Disease Predict Sample POST /api/disease/predict-sample")
        sample_fname = samples[0]["filename"]
        res = client.post("/api/disease/predict-sample", data={"filename": sample_fname})
        assert res.status_code == 200, f"Disease sample predict failed: {res.text}"
        disease_res = res.json()
        print(f"Sample: {sample_fname} -> {disease_res['crop']} | {disease_res['disease']} ({disease_res['confidence_pct']}%)")
        assert disease_res["guidance"] is not None
        print(f"Guidance summary: {disease_res['guidance']['summary'][:60]}...")

        print("\n>>> 9. Testing Encyclopedia GET /api/guidance")
        res = client.get("/api/guidance")
        assert res.status_code == 200
        encyclopedia = res.json()
        print(f"Total encyclopedia entries: {len(encyclopedia)}")
        assert len(encyclopedia) == 38

        print("\n>>> 10. Testing History GET /api/history")
        res = client.get("/api/history")
        assert res.status_code == 200
        history_items = res.json()
        print(f"History entries recorded: {len(history_items)}")
        for item in history_items[:3]:
            print(f"  - [{item['module'].upper()}] {item['prediction_result']}")

        print("\n🎉 ALL 10 REST API ENDPOINT TESTS PASSED WITHOUT ERRORS! 🎉")

if __name__ == "__main__":
    test_all()
