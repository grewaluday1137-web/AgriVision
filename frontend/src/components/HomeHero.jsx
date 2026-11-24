import React from 'react';
import { 
  Stethoscope, 
  Compass, 
  TrendingUp, 
  BookOpen, 
  Sparkles, 
  ShieldCheck, 
  Cpu, 
  CheckCircle2, 
  ArrowRight,
  Database,
  BarChart3,
  Layers
} from 'lucide-react';

export default function HomeHero({ setActiveTab }) {
  const modules = [
    {
      id: 'disease',
      title: 'Plant Doctor',
      badge: 'ResNet9 PyTorch Deep CNN',
      tagline: 'Instant Leaf Pathogen Diagnosis & Cure',
      description: 'Upload an infected leaf photograph or select from 33 test specimens. Detects 38 plant disease classes with actionable organic & chemical remedies.',
      icon: Stethoscope,
      gradient: 'from-emerald-500 to-teal-700',
      bgHover: 'group-hover:border-emerald-500/50',
      specs: ['38 Disease Classes', 'Top-3 Probability Breakdown', 'Curated Treatment Manual']
    },
    {
      id: 'crop',
      title: 'Crop Advisor',
      badge: 'XGBoost Multi-Class',
      tagline: 'Precision Soil & Agro-Climatic Recommendation',
      description: 'Input soil nutrients (N-P-K), pH level, rainfall, and climate metrics to discover the highest-yielding crop matched with soil suitability analysis.',
      icon: Compass,
      gradient: 'from-amber-500 to-orange-700',
      bgHover: 'group-hover:border-amber-500/50',
      specs: ['7 Soil & Climate Inputs', '22 Agricultural Crops', '5 Regional Biome Presets']
    },
    {
      id: 'yield',
      title: 'Yield Forecaster',
      badge: 'Bagging Regressor Ensemble',
      tagline: 'Global FAO Harvest Yield Projection',
      description: 'Forecast agricultural yield across 101 countries and 10 staple crops based on rainfall, pesticide volume, and temperature trends with regional baselines.',
      icon: TrendingUp,
      gradient: 'from-blue-500 to-indigo-700',
      bgHover: 'group-hover:border-blue-500/50',
      specs: ['101 Global Nations', '10 Major Food Crops', 'Triple Unit Conversion (t/ha)']
    }
  ];

  return (
    <div className="space-y-12 pb-16">
      
      {/* Hero Banner */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-emerald-900 via-slate-900 to-slate-950 text-white p-8 sm:p-12 shadow-2xl border border-emerald-800/40">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="absolute bottom-0 left-1/3 -mb-20 w-80 h-80 bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div className="relative z-10 max-w-3xl space-y-6">
          <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-full bg-emerald-500/20 border border-emerald-400/30 text-emerald-300 text-xs font-semibold tracking-wide">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Unified Agricultural Decision Support Engine</span>
          </div>

          <h1 className="text-4xl sm:text-5xl font-extrabold tracking-tight leading-tight">
            Next-Generation AI for <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-amber-300">Precision Agriculture</span>
          </h1>

          <p className="text-slate-300 text-base sm:text-lg leading-relaxed">
            AgriVision combines computer vision, gradient boosted trees, and ensemble regressors 
            into a singular decision dashboard. Protect your fields, identify crop diseases before yield loss, 
            and forecast global harvest trends with calibrated scientific accuracy.
          </p>

          <div className="flex flex-wrap gap-4 pt-2">
            <button
              onClick={() => setActiveTab('disease')}
              className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold shadow-lg shadow-emerald-500/30 transition-all hover:scale-[1.02]"
            >
              <Stethoscope className="w-5 h-5" />
              <span>Diagnose Crop Leaf</span>
              <ArrowRight className="w-4 h-4 ml-1" />
            </button>

            <button
              onClick={() => setActiveTab('crop')}
              className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 text-white font-semibold border border-slate-700 transition-all hover:scale-[1.02]"
            >
              <Compass className="w-5 h-5 text-amber-400" />
              <span>Crop Recommendation</span>
            </button>

            <button
              onClick={() => setActiveTab('encyclopedia')}
              className="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700/80 text-white font-semibold border border-slate-700 transition-all hover:scale-[1.02]"
            >
              <BookOpen className="w-5 h-5 text-teal-400" />
              <span>Plant Disease Library</span>
            </button>
          </div>
        </div>

        {/* Floating Architecture KPI Chips */}
        <div className="mt-10 pt-8 border-t border-slate-800/80 grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div className="space-y-1">
            <div className="text-2xl font-bold text-emerald-400">38</div>
            <div className="text-xs text-slate-400 font-medium">Pathologies & Healthy States</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-bold text-amber-400">22</div>
            <div className="text-xs text-slate-400 font-medium">Recommended Crops</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-bold text-blue-400">101</div>
            <div className="text-xs text-slate-400 font-medium">Global Agricultural Nations</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-bold text-teal-400">CUDA 12.6</div>
            <div className="text-xs text-slate-400 font-medium">GPU Accelerated Inference</div>
          </div>
        </div>
      </section>

      {/* 3 Core Machine Learning Modules Cards */}
      <section className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold text-slate-900 dark:text-white">Intelligent Decision Modules</h2>
          <p className="text-sm text-slate-500 dark:text-slate-400">Select any engine below to start diagnosing or analyzing.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {modules.map((m) => {
            const Icon = m.icon;
            return (
              <div
                key={m.id}
                onClick={() => setActiveTab(m.id)}
                className={`group relative p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition-all duration-200 cursor-pointer flex flex-col justify-between ${m.bgHover}`}
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${m.gradient} flex items-center justify-center text-white shadow-md`}>
                      <Icon className="w-6 h-6" />
                    </div>
                    <span className="text-[11px] font-mono font-medium px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                      {m.badge}
                    </span>
                  </div>

                  <div>
                    <h3 className="text-xl font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors">
                      {m.title}
                    </h3>
                    <p className="text-xs font-semibold text-emerald-600 dark:text-emerald-400 mt-0.5">
                      {m.tagline}
                    </p>
                    <p className="text-sm text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                      {m.description}
                    </p>
                  </div>

                  <ul className="space-y-1.5 pt-2">
                    {m.specs.map((spec, i) => (
                      <li key={i} className="flex items-center text-xs text-slate-600 dark:text-slate-400">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 mr-2 flex-shrink-0" />
                        <span>{spec}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="pt-6 mt-4 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between text-sm font-semibold text-emerald-600 dark:text-emerald-400">
                  <span>Launch Engine</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Agronomic Disclaimer */}
      <section className="rounded-2xl p-4 bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-200/50 dark:border-emerald-800/30 flex items-start space-x-3 text-xs text-emerald-800 dark:text-emerald-300">
        <ShieldCheck className="w-5 h-5 flex-shrink-0 text-emerald-600 dark:text-emerald-400 mt-0.5" />
        <p className="leading-relaxed">
          <strong className="font-semibold">Agricultural Safety & Advisory Notice:</strong> AgriVision AI provides data-driven decision assistance trained on standard benchmark agricultural datasets (PlantVillage, FAOSTAT, and soil classification records). Always consult certified local agricultural extension specialists before applying chemical fungicides or high-concentration fertilizers.
        </p>
      </section>
    </div>
  );
}
