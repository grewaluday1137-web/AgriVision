# 🌾 AgriVision AI — Architecture, App Flow & Working Diagrams

This document provides a visual and structural blueprint of the **AgriVision AI** platform, detailing its system topology, user navigation flow, and exact runtime execution mechanisms across all machine learning engines.

---

## 1. High-Level Multi-Tier Architecture Diagram

The system follows a decoupled, multi-tier enterprise architecture separating client rendering, RESTful API orchestration, accelerated machine learning inference, and data persistence.

```mermaid
flowchart TD
    subgraph "Tier 1: Presentation Tier (Client Layer)"
        UI["React 19 SPA (Vite 6, Port 5173)"]
        UI_Sub1["Tailwind CSS v4 Design System"]
        UI_Sub2["Lucide Reactive Icons"]
        UI_Sub3["Dark / Light Mode Controller"]
        UI_Sub4["1-Click Test Specimen Carousel"]
        UI --> UI_Sub1
        UI --> UI_Sub2
        UI --> UI_Sub3
        UI --> UI_Sub4
    end

    subgraph "Tier 2: Application & API Gateway Tier"
        API["FastAPI ASGI Server (Uvicorn, Port 8000)"]
        Router["API Router (/api)"]
        CORS["CORS Middleware"]
        Lifespan["Lifespan Startup Manager\n(Pre-warms all 3 ML models in memory)"]
        Pydantic["Pydantic v2 Schema Validator"]
        
        API --> CORS
        API --> Lifespan
        API --> Router
        Router --> Pydantic
    end

    subgraph "Tier 3: Machine Learning & Analytical Engine Tier"
        subgraph "Engine A: Plant Doctor"
            AD_Disease["Disease Adapter"]
            Torch_CNN["PyTorch ResNet9 CNN (26.4 MB)\n(CUDA 12.6 on RTX 3050 Laptop GPU)"]
            KB_Engine["Curated Agronomic Knowledge Engine\n(38 Pathology Treatment Records)"]
            AD_Disease --> Torch_CNN
            AD_Disease --> KB_Engine
        end

        subgraph "Engine B: Crop Advisor"
            AD_Crop["Crop Adapter"]
            XGB_Model["XGBoost Multi-Class Classifier (1.67 MB)\n(22 Crop Output Classes)"]
            Heuristic["Soil Adequacy Heuristic Analyzer"]
            AD_Crop --> XGB_Model
            AD_Crop --> Heuristic
        end

        subgraph "Engine C: Yield Forecaster"
            AD_Yield["Yield Adapter"]
            Bagging_Model["Scikit-Learn Bagging Regressor (151 MB)\n(101 Nations, 10 Food Crops)"]
            Baseline["Regional Historical Benchmark Calculator"]
            AD_Yield --> Bagging_Model
            AD_Yield --> Baseline
        end
    end

    subgraph "Tier 4: Storage & Persistence Tier"
        DB_Engine["SQLAlchemy ORM Engine"]
        SQLite[("agrivision.db (SQLite / PostgreSQL)\nTable: prediction_records\nTable: users")]
        Disk_Test["Static Disk Storage\ntest/test/ (33 Leaf Specimens)"]
        DB_Engine --> SQLite
    end

    %% Inter-Tier Connections
    UI -->|HTTP POST / GET / Multipart (via Vite Proxy)| API
    Pydantic -->|Foliage Image Bytes| AD_Disease
    Pydantic -->|7 Soil & Weather Features| AD_Crop
    Pydantic -->|Area, Crop, Rain, Pest, Temp| AD_Yield
    API -->|Session Audit Logging| DB_Engine
    API -->|Serve Specimen Images| Disk_Test
```

---

## 2. User Experience & Application Navigation Flow

This flowchart illustrates how users and evaluators navigate through the web interface, from the landing overview to the specialized functional modules.

```mermaid
flowchart TD
    Start(["User Opens AgriVision AI (http://localhost:5173)"]) --> Landing["Landing Dashboard (HomeHero)\n• System Architecture Overview\n• Real-Time GPU Accelerator Status\n• Key Architecture Metrics (38 Pathologies, 22 Crops, 101 Nations)"]

    Landing --> Choice{"Select Module from Header / Cards"}

    %% Path 1: Plant Doctor
    Choice -->|Click 'Plant Doctor'| M1["Plant Doctor Interface"]
    M1 --> M1_Action{"Input Method"}
    M1_Action -->|Drag & Drop or File Browse| Upload["Upload Leaf Photo (JPG, PNG, WebP)"]
    M1_Action -->|1-Click Test Carousel| PickSample["Select 1 of 33 Sample Leaf Specimens"]
    Upload --> RunM1["Click 'Run Diagnosis'"]
    PickSample --> RunM1Auto["Auto-Executes Inference"]
    RunM1 --> M1_Res["Diagnostic Presentation Card\n• Crop Name & Pathology Identified\n• Health State (Healthy vs Infected)\n• Confidence Meter (%)\n• Top-3 Probability Distribution"]
    RunM1Auto --> M1_Res
    M1_Res --> M1_Draw["3-Tab Treatment Drawer\n• Diagnostic Symptoms\n• Organic & Biological Controls\n• Chemical Fungicides\n• Farm Cultural Prevention"]

    %% Path 2: Crop Advisor
    Choice -->|Click 'Crop Advisor'| M2["Crop Advisor Interface"]
    M2 --> M2_Action{"Input Method"}
    M2_Action -->|1-Click Biome Preset| Preset["Select Preset (e.g., Tropical Monsoon, Dryland, Black Cotton)"]
    M2_Action -->|Manual Sliders| Sliders["Adjust Dual Sliders & Inputs for:\nN, P, K, Temp, Humidity, pH, Rainfall"]
    Preset --> RunM2["Populates Form Inputs"]
    Sliders --> RunM2
    RunM2 --> SubmitCrop["Click 'Recommend Optimal Crop'"]
    SubmitCrop --> M2_Res["Recommendation Results Card\n• Primary Recommended Crop & Probability\n• Top-3 Alternative Crops Comparison Bars\n• Soil Macronutrient Status (High/Low/Optimal)\n• Favorable vs Limiting Factor Advisory"]

    %% Path 3: Yield Forecaster
    Choice -->|Click 'Yield Forecaster'| M3["Yield Forecaster Interface"]
    M3 --> M3_Form["Select Parameters from Backend Manifest:\n• 101 Supported Countries\n• 10 Staple Crops\n• Harvest Year (1990 - 2026)\n• Rainfall, Pesticides & Temperature"]
    M3_Form --> SubmitYield["Click 'Forecast Harvest Yield'"]
    SubmitYield --> M3_Res["Yield Forecast Results Card\n• Metric Tonnes per Hectare (t/ha)\n• Kilograms per Hectare (kg/ha)\n• Hectograms per Hectare (hg/ha)\n• Performance Band (Above/Below/Baseline)\n• Regional Benchmark Note"]

    %% Path 4: Encyclopedia
    Choice -->|Click 'Plant Library'| M4["Plant Disease Encyclopedia"]
    M4 --> M4_Tools["Filter by Crop Pills (Apple, Tomato, etc.) OR Search by Symptom"]
    M4_Tools --> M4_Cards["Browse 38 Pathology Cards"]
    M4_Cards --> M4_Modal["Open Full Agronomic Treatment Protocol Modal"]

    %% Path 5: History
    Choice -->|Click 'History'| M5["Prediction Audit History"]
    M5 --> M5_View["Filter Logs by Module (All, Disease, Crop, Yield)"]
    M5_View --> M5_Export["Export Audit Log to JSON OR Delete Records"]
```

---

## 3. Working Mechanism: Plant Doctor Sequence Diagram

This sequence diagram depicts the exact chronological data flow when diagnosing a crop leaf, including image transformation, CUDA execution, and database persistence.

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Evaluator
    participant React as React Frontend (PlantDoctor.jsx)
    participant Fast as FastAPI Router (/api/disease)
    participant Adapt as DiseaseAdapter
    participant Torch as PyTorch ResNet9 (CUDA GPU)
    participant KB as Agronomic Knowledge Engine
    participant DB as SQLite (agrivision.db)

    User->>React: Uploads leaf photo OR clicks 1-Click Sample Leaf
    React->>Fast: POST /api/disease/predict (multipart/form-data)
    Note over Fast: Validates file type (image/*) and size
    Fast->>Adapt: predict_image_bytes(bytes)
    Note over Adapt: PIL RGB convert -> Resize(256, 256) -> ToTensor()
    Adapt->>Torch: Forward pass: tensor.unsqueeze(0).to(device)
    Note over Torch: Evaluates 9 residual blocks in ~4.2 ms on RTX 3050
    Torch-->>Adapt: 38 raw class logits
    Note over Adapt: Applies torch.softmax(logits, dim=1)<br/>Extracts top_k=3 candidates
    Adapt-->>Fast: Returns crop, disease, is_healthy, confidence, top_predictions
    Fast->>KB: get_disease_guidance(raw_class_name)
    KB-->>Fast: Returns symptoms, organic_controls, chemical_controls, prevention
    Fast->>DB: INSERT INTO prediction_records (module='disease', input_summary, prediction_result, confidence, details_json)
    DB-->>Fast: Commit transaction
    Fast-->>React: 200 OK: DiseasePredictionResponse (JSON)
    React-->>User: Displays diagnostic card, confidence gauge, and treatment drawer
```

---

## 4. Working Mechanism: Crop Advisor Sequence Diagram

This sequence diagram illustrates how the Crop Advisor validates soil macronutrients and environmental drivers, computes multi-class probabilities, and generates agronomic suitability advice.

```mermaid
sequenceDiagram
    autonumber
    actor User as Farmer / Agronomist
    participant React as React Frontend (CropAdvisor.jsx)
    participant Fast as FastAPI Router (/api/crop)
    participant Adapt as CropAdapter
    participant XGB as XGBoost Classifier (CRS.pkl)
    participant DB as SQLite (agrivision.db)

    User->>React: Selects Biome Preset OR adjusts N, P, K, pH, Weather sliders
    User->>React: Clicks "Recommend Optimal Crop"
    React->>Fast: POST /api/crop/recommend (JSON payload)
    Note over Fast: Pydantic validates ranges:<br/>N (0-200), P (0-200), K (0-250), pH (2-12)...
    Fast->>Adapt: predict(nitrogen, phosphorus, potassium, temp, humidity, ph, rainfall)
    Note over Adapt: Assembles DataFrame with feature_names=['N','P','K','temperature','humidity','ph','rainfall']
    Adapt->>XGB: model.predict_proba(input_df)
    XGB-->>Adapt: 22-dimensional probability array
    Note over Adapt: Inverse transforms highest-index via LabelEncoder<br/>Ranks top 3 alternatives<br/>Analyzes pH acidity and NPK sufficiency
    Adapt-->>Fast: Returns recommended_crop, confidence, top_alternatives, soil_suitability_analysis
    Fast->>DB: INSERT INTO prediction_records (module='crop', input_summary, prediction_result, confidence, details_json)
    DB-->>Fast: Commit transaction
    Fast-->>React: 200 OK: CropRecommendationResponse (JSON)
    React-->>User: Renders glowing recommendation card, probability meters, and soil status pills
```

---

## 5. Working Mechanism: Yield Forecaster Sequence Diagram

This sequence diagram shows how the Yield Forecaster validates country/crop inputs against the FAO manifest, performs label encoding, predicts harvest yields, and computes regional performance bands.

```mermaid
sequenceDiagram
    autonumber
    actor User as Analyst / Operator
    participant React as React Frontend (YieldForecaster.jsx)
    participant Fast as FastAPI Router (/api/yield)
    participant Adapt as YieldAdapter
    participant Bag as Bagging Regressor (bagging_regressor.pkl)
    participant DB as SQLite (agrivision.db)

    User->>React: Selects Country (e.g. India), Crop (Potatoes), Year (2024), Rain, Pest, Temp
    User->>React: Clicks "Forecast Harvest Yield"
    React->>Fast: POST /api/yield/predict (JSON payload)
    Note over Fast: Pydantic validates numeric boundaries and field constraints
    Fast->>Adapt: predict(country, crop, year, rainfall_mm, pesticides_tonnes, avg_temp_celsius)
    Note over Adapt: Verifies country in supported 101 countries<br/>Encodes Area via le_area.transform()<br/>Encodes Crop via le_item.transform()
    Adapt->>Bag: model.predict(input_df)
    Bag-->>Adapt: Raw predicted yield in hg/ha (e.g. 222,903.9 hg/ha)
    Note over Adapt: Converts units:<br/>tonnes_ha = hg_ha / 10,000 (22.29 t/ha)<br/>kg_ha = hg_ha / 10 (22,290.4 kg/ha)<br/>Looks up regional benchmark: 18.21 t/ha<br/>Computes Performance Ratio: R = 1.22 -> 'Above Historical Average'
    Adapt-->>Fast: Returns predicted_yield_tonnes, kg, hg, benchmark, performance_band, context_notes
    Fast->>DB: INSERT INTO prediction_records (module='yield', input_summary, prediction_result, confidence, details_json)
    DB-->>Fast: Commit transaction
    Fast-->>React: 200 OK: YieldPredictionResponse (JSON)
    React-->>User: Renders triple-unit yield card, performance band badge, and historical baseline context
```

---

## 6. End-to-End Data State Lifecycle Diagram

This state transition diagram illustrates how data transforms throughout the entire lifecycle of an AgriVision AI user session.

```mermaid
stateDiagram-v2
    [*] --> Idle: App Mounts & Fetches /api/health
    Idle --> ModelPrewarmed: Lifespan Loaded Models into VRAM/RAM
    
    state "Plant Doctor Lifecycle" as PD_Flow {
        Idle --> SpecimenSelected: User Drops Image or Clicks Sample
        SpecimenSelected --> FoliagePreprocessing: File sent to backend
        FoliagePreprocessing --> CudaInference: Tensor on RTX 3050 GPU
        CudaInference --> GuidanceEnrichment: Query 38-class Knowledge Engine
        GuidanceEnrichment --> DiagnosisReady: Render Diagnostics & Treatments
    }

    state "Crop Advisor Lifecycle" as CA_Flow {
        Idle --> SoilParamsEntered: User Sets NPK & Weather Sliders
        SoilParamsEntered --> XGBoostInference: Features formatted into DataFrame
        XGBoostInference --> SuitabilityAnalysis: Evaluate pH and NPK thresholds
        SuitabilityAnalysis --> CropRecommendationReady: Render Best Match & Alternatives
    }

    state "Yield Forecaster Lifecycle" as YF_Flow {
        Idle --> ForecastParamsEntered: Nation, Crop & Weather selected
        ForecastParamsEntered --> LabelEncoding: Categoricals mapped to FAO indices
        LabelEncoding --> BaggingInference: Ensemble tree regression executed
        BaggingInference --> UnitConversion: hg/ha converted to t/ha & kg/ha
        UnitConversion --> YieldProjectionReady: Render Harvest Metrics & Benchmark
    }

    DiagnosisReady --> PersistedToDB: Async SQLite Commit
    CropRecommendationReady --> PersistedToDB: Async SQLite Commit
    YieldProjectionReady --> PersistedToDB: Async SQLite Commit

    PersistedToDB --> HistoryQueried: User Views History & Exports JSON
    HistoryQueried --> Idle: Reset or Next Task
```

---

## 7. Database Entity Relationship (ER) Diagram

The persistence schema captures all diagnostic and predictive workflows into auditable records.

```mermaid
erDiagram
    PREDICTION_RECORD {
        int id PK "Auto-increment primary key"
        string module "Module identifier ('disease', 'crop', 'yield')"
        text input_summary "Plain-text summary of input parameters"
        string prediction_result "Concise string of final prediction"
        float confidence "Model confidence or R2 score (0.0 - 1.0)"
        json details_json "Complete structured JSON payload of inputs & outputs"
        datetime created_at "UTC timestamp of execution"
    }

    USER {
        int id PK "Auto-increment primary key"
        string username "Unique username index"
        string email "Unique email address index"
        string hashed_password "Bcrypt password hash"
        datetime created_at "User registration timestamp"
    }

    USER ||--o{ PREDICTION_RECORD : "records (optional link)"
```
