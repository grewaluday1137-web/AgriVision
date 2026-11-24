import pickle
import logging
import warnings
import pandas as pd
from typing import Dict, Any, List, Optional
from sklearn.preprocessing import LabelEncoder

from app.core.config import YIELD_MODEL_PATH, YIELD_DATASET_PATH

logger = logging.getLogger(__name__)

class YieldForecasterAdapter:
    def __init__(self):
        self.model = None
        self.country_encoder = LabelEncoder()
        self.crop_encoder = LabelEncoder()
        self.countries: List[str] = []
        self.crops: List[str] = []
        self.benchmarks: Dict[str, float] = {}
        self.manifest: Dict[str, Any] = {}
        self.load_model()

    def is_loaded(self) -> bool:
        return self.model is not None and len(self.countries) > 0

    def load_model(self):
        try:
            df = pd.read_csv(YIELD_DATASET_PATH)
            if 'Unnamed: 0' in df.columns:
                df = df.drop('Unnamed: 0', axis=1)

            # Drop countries with less than 100 records
            country_counts = df['Area'].value_counts()
            countries_to_drop = country_counts[country_counts < 100].index.tolist()
            df_filtered = df[~df['Area'].isin(countries_to_drop)].reset_index(drop=True)

            self.country_encoder.fit(df_filtered['Area'])
            self.crop_encoder.fit(df_filtered['Item'])

            self.countries = sorted([str(a) for a in self.country_encoder.classes_])
            self.crops = sorted([str(i) for i in self.crop_encoder.classes_])

            # Calculate historical mean yield per (Area, Item) in hg/ha
            grouped = df_filtered.groupby(['Area', 'Item'])['hg/ha_yield'].mean().to_dict()
            self.benchmarks = {f"{k[0]}::{k[1]}": float(v) for k, v in grouped.items()}

            self.manifest = {
                "supported_countries": self.countries,
                "supported_crops": self.crops,
                "year_range": {"min": 1990, "max": 2026},
                "rainfall_range_mm": {
                    "min": float(df_filtered['average_rain_fall_mm_per_year'].min()),
                    "max": float(df_filtered['average_rain_fall_mm_per_year'].max())
                },
                "pesticides_range_tonnes": {
                    "min": float(df_filtered['pesticides_tonnes'].min()),
                    "max": float(df_filtered['pesticides_tonnes'].max())
                },
                "temp_range_celsius": {
                    "min": float(df_filtered['avg_temp'].min()),
                    "max": float(df_filtered['avg_temp'].max())
                },
                "unit_explanations": {
                    "hg_per_ha": "Hectograms per Hectare (10,000 hg = 1 metric tonne)",
                    "tonnes_per_hectare": "Metric Tonnes per Hectare (Standard agronomic international measure)",
                    "kg_per_ha": "Kilograms per Hectare (1 tonne = 1,000 kg)"
                }
            }

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                with open(YIELD_MODEL_PATH, "rb") as f:
                    self.model = pickle.load(f)

            logger.info(f"Yield Forecaster model loaded ({len(self.countries)} countries, {len(self.crops)} crops).")
        except Exception as e:
            logger.error(f"Failed to load Yield Forecaster model: {e}")
            raise e

    def get_manifest(self) -> Dict[str, Any]:
        return self.manifest

    def predict(
        self,
        country: Optional[str] = None,
        crop: Optional[str] = None,
        year: int = 2024,
        rainfall_mm: float = 1000.0,
        pesticides_tonnes: float = 10000.0,
        avg_temp_celsius: float = 20.0,
        **kwargs
    ) -> Dict[str, Any]:
        if self.model is None:
            raise RuntimeError("Yield Forecaster model is not loaded.")

        # Support alias arguments (area, item, rainfall, pesticides, avg_temp)
        area = country or kwargs.get('area')
        item = crop or kwargs.get('item')
        rain = rainfall_mm if rainfall_mm is not None else kwargs.get('rainfall', kwargs.get('average_rain_fall_mm_per_year', 1000.0))
        pest = pesticides_tonnes if pesticides_tonnes is not None else kwargs.get('pesticides', 10000.0)
        temp = avg_temp_celsius if avg_temp_celsius is not None else kwargs.get('avg_temp', 20.0)

        if not area or area not in self.countries:
            raise ValueError(f"Unsupported Country '{area}'. Supported countries: {len(self.countries)}")
        if not item or item not in self.crops:
            raise ValueError(f"Unsupported Crop '{item}'. Supported crops: {len(self.crops)}")

        area_encoded = self.country_encoder.transform([area])[0]
        item_encoded = self.crop_encoder.transform([item])[0]

        input_data = pd.DataFrame([{
            'Area': area_encoded,
            'Item': item_encoded,
            'Year': int(year),
            'average_rain_fall_mm_per_year': float(rain),
            'pesticides_tonnes': float(pest),
            'avg_temp': float(temp)
        }])

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            predicted_hg_ha = float(self.model.predict(input_data)[0])

        # Unit conversions: 1 tonne = 10,000 hg, 1 kg = 10 hg
        tonnes_ha = round(predicted_hg_ha / 10000.0, 2)
        kg_ha = round(predicted_hg_ha / 10.0, 1)

        # Historical benchmark lookup
        benchmark_key = f"{area}::{item}"
        benchmark_hg_ha = self.benchmarks.get(benchmark_key)

        if benchmark_hg_ha is not None and benchmark_hg_ha > 0:
            ratio = predicted_hg_ha / benchmark_hg_ha
            if ratio >= 1.15:
                performance = "Above Historical Average"
            elif ratio <= 0.85:
                performance = "Below Historical Average"
            else:
                performance = "Consistent with Regional Baseline"
            context = (
                f"Predicted harvest of {tonnes_ha} tonnes/ha is {performance.lower()} "
                f"for {item} in {area} (historical benchmark: {benchmark_hg_ha / 10000.0:.2f} tonnes/ha)."
            )
        else:
            performance = "Projected Estimate"
            context = f"Projected harvest of {tonnes_ha} tonnes/ha calculated from agro-climatic conditions for {item} in {area}."

        return {
            "country": area,
            "crop": item,
            "year": int(year),
            "predicted_yield_hg_per_ha": round(predicted_hg_ha, 1),
            "predicted_yield_tonnes_per_hectare": tonnes_ha,
            "predicted_yield_kg_per_ha": kg_ha,
            "historical_benchmark_hg_ha": round(benchmark_hg_ha, 1) if benchmark_hg_ha else None,
            "performance_band": performance,
            "context_notes": context
        }

yield_adapter = YieldForecasterAdapter()
