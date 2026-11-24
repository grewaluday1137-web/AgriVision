import React, { useState, useEffect } from 'react';
import { 
  TrendingUp, 
  Globe, 
  Calendar, 
  CloudRain, 
  Thermometer, 
  FlaskConical, 
  Sparkles, 
  RefreshCw, 
  AlertCircle,
  BarChart3,
  Award,
  HelpCircle,
  Info
} from 'lucide-react';
import { api } from '../api/client';

export default function YieldForecaster() {
  const [manifest, setManifest] = useState(null);
  const [loadingManifest, setLoadingManifest] = useState(true);

  const [formData, setFormData] = useState({
    country: 'India',
    crop: 'Potatoes',
    year: 2024,
    rainfall_mm: 1083.0,
    pesticides_tonnes: 50000.0,
    avg_temp_celsius: 26.5
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.getYieldManifest()
      .then(data => {
        setManifest(data);
        setLoadingManifest(false);
        // Default to first country and crop if present
        if (data.supported_countries?.length > 0 && !data.supported_countries.includes(formData.country)) {
          setFormData(prev => ({ ...prev, country: data.supported_countries[0] }));
        }
      })
      .catch(err => {
        console.error("Failed to load yield manifest:", err);
        setLoadingManifest(false);
      });
  }, []);

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: field === 'country' || field === 'crop' ? value : (parseFloat(value) || 0)
    }));
  };

  const handlePredict = async (e) => {
    e?.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await api.predictYield(formData);
      setResult(res);
    } catch (err) {
      setError(err.message || 'Harvest yield forecasting failed.');
    } finally {
      setLoading(false);
    }
  };

  // Performance band color badge
  const getBandBadge = (band) => {
    if (!band) return 'bg-slate-100 text-slate-800';
    if (band.includes('Above')) return 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border-emerald-300';
    if (band.includes('Below')) return 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border-amber-300';
    return 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300 border-blue-300';
  };

  return (
    <div className="space-y-8 pb-16">
      
      {/* Header */}
      <div>
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-950/70 text-blue-800 dark:text-blue-300 text-xs font-semibold mb-2">
          <TrendingUp className="w-3.5 h-3.5" />
          <span>Bagging Regressor Ensemble (FAO Global Dataset)</span>
        </div>
        <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white">
          Harvest Yield Forecaster
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Predict expected crop harvest yield (tonnes/ha) based on international agro-climatic conditions, 
          fertilizer/pesticide volume, rainfall patterns, and historical regional baselines.
        </p>
      </div>

      {/* Main Grid: Form on Left (6 cols), Projections on Right (6 cols) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Form: Geographic & Climatic Inputs */}
        <div className="lg:col-span-6 space-y-6">
          <div className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-6">
            
            {/* Country & Crop Selectors */}
            <div className="space-y-4">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300 flex items-center border-b border-slate-100 dark:border-slate-800 pb-2">
                <Globe className="w-3.5 h-3.5 mr-1.5 text-blue-500" />
                Target Nation & Commodity Crop
              </span>

              {/* Country Selection */}
              <div className="space-y-1.5">
                <label className="text-xs font-semibold text-slate-700 dark:text-slate-300">
                  Country / Region ({manifest?.supported_countries?.length || 0} Supported)
                </label>
                <select
                  value={formData.country}
                  onChange={(e) => handleInputChange('country', e.target.value)}
                  className="w-full text-xs px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white font-medium focus:outline-none focus:ring-1 focus:ring-blue-500"
                >
                  {manifest?.supported_countries?.map((c) => (
                    <option key={c} value={c}>{c}</option>
                  ))}
                </select>
              </div>

              {/* Crop Selection */}
              <div className="space-y-1.5">
                <label className="text-xs font-semibold text-slate-700 dark:text-slate-300">
                  Staple Food Commodity ({manifest?.supported_crops?.length || 0} Crops)
                </label>
                <select
                  value={formData.crop}
                  onChange={(e) => handleInputChange('crop', e.target.value)}
                  className="w-full text-xs px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white font-medium focus:outline-none focus:ring-1 focus:ring-blue-500"
                >
                  {manifest?.supported_crops?.map((crop) => (
                    <option key={crop} value={crop}>{crop}</option>
                  ))}
                </select>
              </div>

              {/* Harvest Year Slider */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300 flex items-center space-x-1.5">
                    <Calendar className="w-3.5 h-3.5 text-slate-400" />
                    <span>Harvest Year</span>
                  </label>
                  <input 
                    type="number" 
                    min="1990" 
                    max="2026" 
                    value={formData.year}
                    onChange={(e) => handleInputChange('year', e.target.value)}
                    className="w-20 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                  />
                </div>
                <input 
                  type="range" 
                  min="1990" 
                  max="2026" 
                  value={formData.year}
                  onChange={(e) => handleInputChange('year', e.target.value)}
                  className="w-full accent-blue-500"
                />
              </div>
            </div>

            {/* Environmental & Agronomic Drivers */}
            <div className="space-y-4 pt-2">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300 flex items-center border-b border-slate-100 dark:border-slate-800 pb-2">
                <CloudRain className="w-3.5 h-3.5 mr-1.5 text-teal-500" />
                Agronomic Drivers & Meteorology
              </span>

              {/* Rainfall */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Average Rainfall (Annual)
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="50" 
                      max="3500" 
                      step="10"
                      value={formData.rainfall_mm}
                      onChange={(e) => handleInputChange('rainfall_mm', e.target.value)}
                      className="w-20 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">mm</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="50" 
                  max="3500" 
                  step="25"
                  value={formData.rainfall_mm}
                  onChange={(e) => handleInputChange('rainfall_mm', e.target.value)}
                  className="w-full accent-blue-500"
                />
              </div>

              {/* Pesticides */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300 flex items-center space-x-1">
                    <FlaskConical className="w-3.5 h-3.5 text-purple-400" />
                    <span>Pesticide Application</span>
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="0" 
                      max="150000" 
                      step="500"
                      value={formData.pesticides_tonnes}
                      onChange={(e) => handleInputChange('pesticides_tonnes', e.target.value)}
                      className="w-24 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">tonnes</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="0" 
                  max="100000" 
                  step="500"
                  value={formData.pesticides_tonnes}
                  onChange={(e) => handleInputChange('pesticides_tonnes', e.target.value)}
                  className="w-full accent-blue-500"
                />
              </div>

              {/* Temperature */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300 flex items-center space-x-1">
                    <Thermometer className="w-3.5 h-3.5 text-rose-400" />
                    <span>Average Temperature</span>
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="-5" 
                      max="40" 
                      step="0.5"
                      value={formData.avg_temp_celsius}
                      onChange={(e) => handleInputChange('avg_temp_celsius', e.target.value)}
                      className="w-20 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">°C</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="-2" 
                  max="38" 
                  step="0.5"
                  value={formData.avg_temp_celsius}
                  onChange={(e) => handleInputChange('avg_temp_celsius', e.target.value)}
                  className="w-full accent-blue-500"
                />
              </div>
            </div>

            {/* Predict Button */}
            <button
              onClick={handlePredict}
              disabled={loading}
              className="w-full py-3.5 px-4 rounded-xl bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white font-bold shadow-lg shadow-blue-600/25 flex items-center justify-center space-x-2 transition-all hover:scale-[1.01]"
            >
              {loading ? (
                <>
                  <RefreshCw className="w-5 h-5 animate-spin" />
                  <span>Computing Bagging Regressor...</span>
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  <span>Forecast Harvest Yield</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* Right Column: Forecast Results & Metrics */}
        <div className="lg:col-span-6 space-y-6">
          
          {error && (
            <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 text-rose-800 dark:text-rose-200 text-sm flex items-start space-x-3">
              <AlertCircle className="w-5 h-5 flex-shrink-0 text-rose-600 dark:text-rose-400 mt-0.5" />
              <div>
                <p className="font-semibold">Prediction Error</p>
                <p className="text-xs mt-1">{error}</p>
              </div>
            </div>
          )}

          {result ? (
            <div className="space-y-6 animate-fadeIn">
              
              {/* Primary Yield Card */}
              <div className="rounded-2xl p-6 bg-gradient-to-br from-blue-50 via-indigo-50 to-white dark:from-blue-950/60 dark:via-slate-900 dark:to-slate-900 border border-blue-300 dark:border-blue-800 shadow-md">
                <div className="flex items-start justify-between">
                  <div>
                    <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold bg-blue-100 text-blue-800 dark:bg-blue-900/80 dark:text-blue-200">
                      <Award className="w-3.5 h-3.5" />
                      <span>{result.country} • {result.year}</span>
                    </span>

                    <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-3">
                      {result.crop} Yield Forecast
                    </h2>
                  </div>

                  <span className={`text-xs px-2.5 py-1 rounded-full font-bold border ${getBandBadge(result.performance_band)}`}>
                    {result.performance_band}
                  </span>
                </div>

                {/* Triple-Unit Yield Highlights */}
                <div className="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-3">
                  
                  {/* Metric Tonnes / Ha */}
                  <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-800/90 border border-blue-200/80 dark:border-slate-700 shadow-sm">
                    <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                      Tonnes per Hectare
                    </span>
                    <span className="text-2xl font-black text-blue-600 dark:text-blue-400 mt-1 block">
                      {result.predicted_yield_tonnes_per_hectare}
                    </span>
                    <span className="text-[10px] text-slate-500 dark:text-slate-400">t / ha (Standard Metric)</span>
                  </div>

                  {/* Kilograms / Ha */}
                  <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-800/90 border border-blue-200/80 dark:border-slate-700 shadow-sm">
                    <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                      Kilograms per Ha
                    </span>
                    <span className="text-xl font-black text-slate-800 dark:text-slate-200 mt-1 block">
                      {result.predicted_yield_kg_per_ha.toLocaleString()}
                    </span>
                    <span className="text-[10px] text-slate-500 dark:text-slate-400">kg / ha</span>
                  </div>

                  {/* Hectograms / Ha */}
                  <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-800/90 border border-blue-200/80 dark:border-slate-700 shadow-sm">
                    <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                      Hectograms per Ha
                    </span>
                    <span className="text-xl font-black text-slate-800 dark:text-slate-200 mt-1 block">
                      {result.predicted_yield_hg_per_ha.toLocaleString()}
                    </span>
                    <span className="text-[10px] text-slate-500 dark:text-slate-400">hg / ha (FAO Base)</span>
                  </div>
                </div>

                {/* Context & Benchmark Note */}
                <div className="mt-6 pt-4 border-t border-blue-200/60 dark:border-slate-800">
                  <p className="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
                    {result.context_notes}
                  </p>
                </div>
              </div>

              {/* Technical Units Reference Card */}
              <div className="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300 flex items-center">
                  <Info className="w-3.5 h-3.5 mr-1.5 text-blue-500" />
                  International Measurement Standards:
                </h4>
                <ul className="space-y-1.5 text-xs text-slate-600 dark:text-slate-400">
                  <li className="flex items-center space-x-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                    <span><strong>1 Metric Tonne</strong> = 10,000 Hectograms (hg) = 1,000 Kilograms (kg).</span>
                  </li>
                  <li className="flex items-center space-x-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                    <span><strong>Hectograms per hectare (hg/ha)</strong> is the official statistical reporting unit of the Food and Agriculture Organization (FAO).</span>
                  </li>
                </ul>
              </div>
            </div>
          ) : (
            /* Empty State */
            <div className="h-full min-h-[380px] rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 flex flex-col items-center justify-center text-center space-y-4 shadow-sm">
              <div className="w-16 h-16 rounded-2xl bg-blue-50 dark:bg-blue-950/50 text-blue-600 dark:text-blue-400 flex items-center justify-center">
                <TrendingUp className="w-8 h-8" />
              </div>
              <div className="max-w-md">
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                  Awaiting Forecast Parameters
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                  Select your country and crop from the selectors on the left, then click "Forecast Harvest Yield" 
                  to run the Bagging Regressor ensemble model trained on global FAO agricultural statistics.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
