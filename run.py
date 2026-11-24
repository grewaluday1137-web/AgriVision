"""
AgriVision AI — Unified Single-Command Runner
Launches both the FastAPI backend (port 8000) and the Vite React frontend (port 5173).
"""

import os
import sys
import time
import subprocess
import signal

PYTHON_EXE = sys.executable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

def print_banner():
    banner = """
========================================================================
   🌾 AgriVision AI — Agricultural Decision Support Platform
========================================================================
   🌱 Plant Doctor      : ResNet9 Deep CNN (38 Disease Classes)
   🧭 Crop Advisor      : XGBoost Classifier (22 Crops + Soil NPK)
   📈 Yield Forecaster  : Bagging Regressor (101 Nations, FAO)
   📖 Plant Library     : 38 Comprehensive Agronomic Cures & Symptoms
========================================================================
    🚀 Web Application  : http://localhost:5173
    📖 API Documentation: http://localhost:8000/docs
    🩺 System Health    : http://localhost:8000/api/health
========================================================================
    Press Ctrl+C to terminate both servers.
========================================================================
"""
    print(banner)

def main():
    print_banner()

    # Environment variables
    env = os.environ.copy()
    env["PYTHONPATH"] = BACKEND_DIR

    processes = []

    try:
        # 1. Start FastAPI Backend Server
        print("▶ Starting FastAPI Backend Server on port 8000...")
        backend_cmd = [
            PYTHON_EXE,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
            "--reload"
        ]
        backend_proc = subprocess.Popen(
            backend_cmd,
            cwd=BACKEND_DIR,
            env=env
        )
        processes.append(backend_proc)

        # Allow backend to initialize database & warm up models
        time.sleep(2)

        # 2. Start Vite Frontend Development Server
        print("▶ Starting Vite React Frontend on port 5173...")
        npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
        frontend_proc = subprocess.Popen(
            [npm_cmd, "run", "dev", "--", "--host"],
            cwd=FRONTEND_DIR,
            env=env
        )
        processes.append(frontend_proc)

        print("\n✅ Both servers are online and communicating.")
        print("💡 Open your browser at: http://localhost:5173\n")

        # Keep running until Ctrl+C
        while True:
            time.sleep(1)
            for p in processes:
                if p.poll() is not None:
                    print(f"\n[Notice] Process {p.args} exited with code {p.returncode}")
                    return

    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down AgriVision AI services...")
    finally:
        for p in processes:
            try:
                if os.name == "nt":
                    p.terminate()
                else:
                    p.send_signal(signal.SIGINT)
            except Exception:
                pass
        print("👋 AgriVision AI shutdown complete.")

if __name__ == "__main__":
    main()
