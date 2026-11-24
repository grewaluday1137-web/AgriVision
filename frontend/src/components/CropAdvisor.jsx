import React, { useState, useEffect } from 'react';
import { 
  Compass, 
  Sparkles, 
  RefreshCw, 
  CheckCircle2, 
  AlertCircle, 
  Info, 
  Layers, 
  Sliders, 
  Check, 
  ArrowRight,
  TrendingUp,
  Droplet
} from 'lucide-react';
import { api } from '../api/client';

export default function CropAdvisor() {
  const [formData, setFormData] = useState({
    nitrogen: 90,
    phosphorus: 42,
    potassium: 43,
    temperature: 23.5,
    humidity: 82.0,
    ph: 6.5,
    rainfall: 202.9,
  });

  const [presets, setPresets] = useState([]);
  const [activePreset, setActivePreset] = useState('monsoon_wetland');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.getCropPresets()
      .then(data => {
        setPresets(data);
        if (data.length > 0) {
          setFormData(data[0].data);
          setActivePreset(data[0].id);
        }
      })
      .catch(err => console.error("Failed to load crop presets:", err));
  }, []);

  const handleInputChange = (field, value) => {
    setActivePreset(null); // Clear selected preset if customized
    setFormData(prev => ({
      ...prev,
      [field]: parseFloat(value) || 0
    }));
  };

  const applyPreset = (preset) => {
    setActivePreset(preset.id);
    setFormData(preset.data);
    setResult(null);
  };

  const handleRecommend = async (e) => {
    e?.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await api.recommendCrop(formData);
      setResult(res);
    } catch (err) {
      setError(err.message || 'Crop recommendation failed.');
    } finally {
      setLoading(false);
    }
  };

  // Compute pH color tag
  const getPhColor = (ph) => {
    if (ph < 6.0) return 'text-amber-500 bg-amber-50 dark:bg-amber-950/40 border-amber-300';
    if (ph > 7.5) return 'text-blue-500 bg-blue-50 dark:bg-blue-950/40 border-blue-300';
    return 'text-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300';
  };

  return (
    <div className="space-y-8 pb-16">
      
      {/* Header */}
      <div>
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300 text-xs font-semibold mb-2">
          <Compass className="w-3.5 h-3.5" />
          <span>XGBoost Multi-Class Agricultural Classifier</span>
        </div>
        <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white">
          Crop Advisor & Soil Matching
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Simulate soil macro-nutrients (N-P-K), pH, and ambient meteorological variables to discover 
          the optimum crop profile with multi-alternative probabilities.
        </p>
      </div>

      {/* 1-Click Biome Presets */}
      <div className="space-y-2">
        <span className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 block">
          1-Click Soil & Biome Presets:
        </span>
        <div className="flex flex-wrap gap-2.5">
          {presets.map((p) => {
            const isSelected = activePreset === p.id;
            return (
              <button
                key={p.id}
                onClick={() => applyPreset(p)}
                className={`px-3.5 py-2 rounded-xl text-xs font-semibold border transition-all flex items-center space-x-2 ${
                  isSelected
                    ? 'bg-amber-500 text-slate-950 border-amber-500 shadow-md shadow-amber-500/20'
                    : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:border-amber-400'
                }`}
              >
                {isSelected && <Check className="w-3.5 h-3.5" />}
                <span>{p.name}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Main Grid: Input Form on Left (6 cols), Recommendation Result on Right (6 cols) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Form: Sliders & Parameter Controls */}
        <div className="lg:col-span-6 space-y-6">
          <div className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-6">
            
            {/* Soil Nutrients Section */}
            <div className="space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300 flex items-center">
                  <Layers className="w-3.5 h-3.5 mr-1.5 text-amber-500" />
                  Soil Macronutrients (kg / ha)
                </span>
                <span className="text-[11px] text-slate-400 font-medium">Standard Agronomic Soil Profile</span>
              </div>

              {/* Nitrogen */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Nitrogen (N)
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="0" 
                      max="150" 
                      value={formData.nitrogen}
                      onChange={(e) => handleInputChange('nitrogen', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">kg/ha</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="0" 
                  max="140" 
                  step="1"
                  value={formData.nitrogen}
                  onChange={(e) => handleInputChange('nitrogen', e.target.value)}
                  className="w-full accent-amber-500"
                />
              </div>

              {/* Phosphorus */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Phosphorus (P)
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="0" 
                      max="150" 
                      value={formData.phosphorus}
                      onChange={(e) => handleInputChange('phosphorus', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">kg/ha</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="5" 
                  max="145" 
                  step="1"
                  value={formData.phosphorus}
                  onChange={(e) => handleInputChange('phosphorus', e.target.value)}
                  className="w-full accent-amber-500"
                />
              </div>

              {/* Potassium */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Potassium (K)
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="0" 
                      max="210" 
                      value={formData.potassium}
                      onChange={(e) => handleInputChange('potassium', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">kg/ha</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="5" 
                  max="205" 
                  step="1"
                  value={formData.potassium}
                  onChange={(e) => handleInputChange('potassium', e.target.value)}
                  className="w-full accent-amber-500"
                />
              </div>
            </div>

            {/* Environmental & Meteorological Factors Section */}
            <div className="space-y-4 pt-2">
              <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-300 flex items-center">
                  <Sliders className="w-3.5 h-3.5 mr-1.5 text-teal-500" />
                  Climatic & Soil pH Parameters
                </span>
                <span className="text-[11px] text-slate-400 font-medium">Ambient Growing Conditions</span>
              </div>

              {/* Temperature */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Ambient Temperature
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="5" 
                      max="50" 
                      step="0.5"
                      value={formData.temperature}
                      onChange={(e) => handleInputChange('temperature', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">°C</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="8" 
                  max="45" 
                  step="0.5"
                  value={formData.temperature}
                  onChange={(e) => handleInputChange('temperature', e.target.value)}
                  className="w-full accent-teal-500"
                />
              </div>

              {/* Humidity */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Relative Humidity
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="10" 
                      max="100" 
                      step="1"
                      value={formData.humidity}
                      onChange={(e) => handleInputChange('humidity', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">%</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="14" 
                  max="100" 
                  step="1"
                  value={formData.humidity}
                  onChange={(e) => handleInputChange('humidity', e.target.value)}
                  className="w-full accent-teal-500"
                />
              </div>

              {/* Soil pH */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300 flex items-center space-x-1">
                    <span>Soil Reaction (pH Level)</span>
                    <span className={`text-[10px] px-1.5 py-0.2 rounded border font-mono font-bold ${getPhColor(formData.ph)}`}>
                      {formData.ph < 6 ? 'Acidic' : (formData.ph > 7.5 ? 'Alkaline' : 'Optimal Neutral')}
                    </span>
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="3.5" 
                      max="10" 
                      step="0.1"
                      value={formData.ph}
                      onChange={(e) => handleInputChange('ph', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">pH</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="3.5" 
                  max="9.9" 
                  step="0.1"
                  value={formData.ph}
                  onChange={(e) => handleInputChange('ph', e.target.value)}
                  className="w-full accent-teal-500"
                />
              </div>

              {/* Rainfall */}
              <div className="space-y-1.5">
                <div className="flex justify-between items-center text-xs">
                  <label className="font-semibold text-slate-700 dark:text-slate-300">
                    Annual Precipitation
                  </label>
                  <div className="flex items-center space-x-1">
                    <input 
                      type="number" 
                      min="20" 
                      max="300" 
                      step="1"
                      value={formData.rainfall}
                      onChange={(e) => handleInputChange('rainfall', e.target.value)}
                      className="w-16 px-2 py-0.5 text-right font-mono font-bold text-xs rounded border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white"
                    />
                    <span className="text-[10px] text-slate-400">mm</span>
                  </div>
                </div>
                <input 
                  type="range" 
                  min="20" 
                  max="300" 
                  step="1"
                  value={formData.rainfall}
                  onChange={(e) => handleInputChange('rainfall', e.target.value)}
                  className="w-full accent-teal-500"
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              onClick={handleRecommend}
              disabled={loading}
              className="w-full py-3.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-400 disabled:opacity-50 text-slate-950 font-bold shadow-lg shadow-amber-500/25 flex items-center justify-center space-x-2 transition-all hover:scale-[1.01]"
            >
              {loading ? (
                <>
                  <RefreshCw className="w-5 h-5 animate-spin" />
                  <span>Evaluating XGBoost Classifier...</span>
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  <span>Recommend Optimal Crop</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* Right Column: Recommendation & Agronomic Insights */}
        <div className="lg:col-span-6 space-y-6">
          
          {error && (
            <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 text-rose-800 dark:text-rose-200 text-sm flex items-start space-x-3">
              <AlertCircle className="w-5 h-5 flex-shrink-0 text-rose-600 dark:text-rose-400 mt-0.5" />
              <div>
                <p className="font-semibold">Calculation Error</p>
                <p className="text-xs mt-1">{error}</p>
              </div>
            </div>
          )}

          {result ? (
            <div className="space-y-6 animate-fadeIn">
              
              {/* Primary Recommended Crop Card */}
              <div className="rounded-2xl p-6 bg-gradient-to-br from-amber-50 via-orange-50 to-white dark:from-amber-950/60 dark:via-slate-900 dark:to-slate-900 border border-amber-300 dark:border-amber-800 shadow-md">
                <div className="flex items-start justify-between">
                  <div>
                    <span className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-200/80 dark:bg-amber-900/80 text-amber-900 dark:text-amber-200">
                      <Sparkles className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
                      <span>Best Matched Crop</span>
                    </span>

                    <h2 className="text-3xl sm:text-4xl font-black text-slate-900 dark:text-white mt-3">
                      {result.recommended_crop}
                    </h2>

                    <p className="text-xs text-slate-600 dark:text-slate-300 mt-1">
                      Highest probability match calculated across all 22 crop profiles.
                    </p>
                  </div>

                  {/* Confidence Pill */}
                  <div className="text-right bg-white/90 dark:bg-slate-800/90 p-3.5 rounded-xl border border-amber-200/80 dark:border-slate-700">
                    <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Suitability</span>
                    <span className="text-3xl font-black text-amber-600 dark:text-amber-400">
                      {result.confidence_pct}%
                    </span>
                  </div>
                </div>

                {/* Alternative Crops Breakdown */}
                {result.top_alternatives && result.top_alternatives.length > 1 && (
                  <div className="mt-6 pt-4 border-t border-amber-200/60 dark:border-slate-800">
                    <span className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 block mb-2.5">
                      Top Alternative Crop Candidates:
                    </span>
                    <div className="space-y-2">
                      {result.top_alternatives.slice(1, 4).map((alt, i) => (
                        <div key={i} className="flex items-center justify-between text-xs bg-white/60 dark:bg-slate-800/60 p-2.5 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                          <span className="font-semibold text-slate-800 dark:text-slate-200">{alt.crop}</span>
                          <div className="flex items-center space-x-2">
                            <div className="w-24 h-1.5 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                              <div 
                                className="h-full bg-amber-500 rounded-full"
                                style={{ width: `${Math.max(4, alt.confidence_pct)}%` }}
                              ></div>
                            </div>
                            <span className="font-mono font-bold text-slate-600 dark:text-slate-400 w-12 text-right">
                              {alt.confidence_pct}%
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Soil Suitability Analysis Card */}
              {result.soil_suitability_analysis && (
                <div className="rounded-2xl p-6 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
                  <h3 className="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-wider flex items-center">
                    <Info className="w-4 h-4 mr-2 text-amber-500" />
                    Agronomic Soil & Factor Assessment
                  </h3>

                  {/* Status Pills */}
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center">
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700">
                      <span className="text-[10px] text-slate-400 block">Nitrogen</span>
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {result.soil_suitability_analysis.nitrogen_status}
                      </span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700">
                      <span className="text-[10px] text-slate-400 block">Phosphorus</span>
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {result.soil_suitability_analysis.phosphorus_status}
                      </span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700">
                      <span className="text-[10px] text-slate-400 block">Potassium</span>
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {result.soil_suitability_analysis.potassium_status}
                      </span>
                    </div>
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700">
                      <span className="text-[10px] text-slate-400 block">Soil Reaction</span>
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {result.soil_suitability_analysis.ph_category}
                      </span>
                    </div>
                  </div>

                  {/* Favorable Factors */}
                  {result.soil_suitability_analysis.favorable_factors?.length > 0 && (
                    <div className="space-y-1.5 pt-2">
                      <span className="text-xs font-bold text-emerald-700 dark:text-emerald-400 block">
                        Favorable Cultivation Factors:
                      </span>
                      {result.soil_suitability_analysis.favorable_factors.map((fav, i) => (
                        <div key={i} className="flex items-start text-xs text-slate-600 dark:text-slate-300">
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 mr-2 flex-shrink-0 mt-0.5" />
                          <span>{fav}</span>
                        </div>
                      ))}
                    </div>
                  )}

                  {/* Limiting Factors / Recommendations */}
                  {result.soil_suitability_analysis.limiting_factors?.length > 0 && (
                    <div className="space-y-1.5 pt-2">
                      <span className="text-xs font-bold text-amber-700 dark:text-amber-400 block">
                        Agronomic Challenges & Soil Amendments:
                      </span>
                      {result.soil_suitability_analysis.limiting_factors.map((lim, i) => (
                        <div key={i} className="flex items-start text-xs text-slate-600 dark:text-slate-300">
                          <AlertCircle className="w-3.5 h-3.5 text-amber-500 mr-2 flex-shrink-0 mt-0.5" />
                          <span>{lim}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
          ) : (
            /* Empty State */
            <div className="h-full min-h-[380px] rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 flex flex-col items-center justify-center text-center space-y-4 shadow-sm">
              <div className="w-16 h-16 rounded-2xl bg-amber-50 dark:bg-amber-950/50 text-amber-600 dark:text-amber-400 flex items-center justify-center">
                <Compass className="w-8 h-8" />
              </div>
              <div className="max-w-md">
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                  Awaiting Soil & Climate Inputs
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                  Select a biome preset from the top or adjust the N-P-K nutrient sliders on the left, 
                  then click "Recommend Optimal Crop" to query the XGBoost decision engine.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
