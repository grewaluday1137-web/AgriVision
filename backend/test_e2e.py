"""
End-to-End System Integration and Accuracy Verification for AgriVision AI.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from fastapi.testclient import TestClient
from app.main import app

def run_e2e_verification():
    print("=" * 60)
    print("🌱 AgriVision AI — End-to-End System Verification")
    print("=" * 60)

    with TestClient(app) as client:
        # 1. System Health & GPU Status
        health_res = client.get("/api/health")
        assert health_res.status_code == 200
        health = health_res.json()
        print(f"1. Health Check: Status='{health['status']}', Device='{health['device']}'")
        assert health["models_loaded"]["plant_disease_resnet9"] == True
        assert health["models_loaded"]["crop_recommender_xgboost"] == True
        assert health["models_loaded"]["yield_predictor_bagging"] == True

        # 2. Plant Doctor: 1-Click Sample & Guidance Check
        samples_res = client.get("/api/disease/samples")
        assert samples_res.status_code == 200
        samples = samples_res.json()
        assert len(samples) >= 30, f"Expected 30+ sample images, got {len(samples)}"
        print(f"2. Plant Doctor Samples: Found {len(samples)} valid leaf specimens.")

        # Test inference on sample
        test_sample = samples[0]["filename"]
        pred_res = client.post("/api/disease/predict-sample", data={"filename": test_sample, "notes": "E2E Automated Test"})
        assert pred_res.status_code == 200
        pred = pred_res.json()
        print(f"   Inference on '{test_sample}': Result='{pred['crop']} — {pred['disease']}', Confidence={pred['confidence_pct']}%")
        assert pred["confidence"] >= 0.5
        assert pred["guidance"] is not None
        assert len(pred["guidance"]["symptoms"]) > 0
        assert len(pred["guidance"]["organic_treatments"]) > 0
        print("   Agronomic Guidance: Verified symptoms and organic controls attached.")

        # 3. Crop Advisor: Preset & Custom Soil Simulation
        presets_res = client.get("/api/crop/presets")
        assert presets_res.status_code == 200
        presets = presets_res.json()
        assert len(presets) == 5
        print(f"3. Crop Advisor: Verified {len(presets)} agronomic biome presets.")

        rec_res = client.post("/api/crop/recommend", json=presets[0]["data"])
        assert rec_res.status_code == 200
        rec = rec_res.json()
        print(f"   Recommendation for '{presets[0]['name']}': '{rec['recommended_crop']}' ({rec['confidence_pct']}%)")
        assert len(rec["top_alternatives"]) >= 3
        assert "nitrogen_status" in rec["soil_suitability_analysis"]

        # 4. Yield Forecaster: Global Manifest & Projection
        manifest_res = client.get("/api/yield/manifest")
        assert manifest_res.status_code == 200
        manifest = manifest_res.json()
        print(f"4. Yield Forecaster Manifest: {len(manifest['supported_countries'])} countries, {len(manifest['supported_crops'])} crops.")
        assert "India" in manifest["supported_countries"]
        assert "Potatoes" in manifest["supported_crops"]

        yield_res = client.post("/api/yield/predict", json={
            "country": "India",
            "crop": "Potatoes",
            "year": 2024,
            "rainfall_mm": 1100.0,
            "pesticides_tonnes": 52000.0,
            "avg_temp_celsius": 26.0
        })
        assert yield_res.status_code == 200
        y_data = yield_res.json()
        print(f"   Yield Projection: {y_data['predicted_yield_tonnes_per_hectare']} tonnes/ha ({y_data['performance_band']})")
        assert y_data["predicted_yield_tonnes_per_hectare"] > 0

        # 5. Agronomic Encyclopedia
        guidance_res = client.get("/api/guidance")
        assert guidance_res.status_code == 200
        all_guidance = guidance_res.json()
        print(f"5. Plant Disease Library: {len(all_guidance)} full pathology protocols available.")
        assert len(all_guidance) == 38

        # 6. Audit & History Record Logging
        history_res = client.get("/api/history")
        assert history_res.status_code == 200
        hist = history_res.json()
        print(f"6. Prediction History: {len(hist)} records securely persisted in database.")
        assert len(hist) > 0

    print("=" * 60)
    print("🏆 ALL END-TO-END VERIFICATION CHECKS PASSED PERFECTLY! 🏆")
    print("=" * 60)

if __name__ == "__main__":
    run_e2e_verification()
