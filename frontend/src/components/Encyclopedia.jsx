import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Search, 
  Leaf, 
  CheckCircle2, 
  AlertTriangle, 
  Droplet, 
  ShieldAlert, 
  RefreshCw,
  X,
  ExternalLink
} from 'lucide-react';
import { api } from '../api/client';

export default function Encyclopedia() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedCrop, setSelectedCrop] = useState('');
  const [activeItem, setActiveItem] = useState(null); // Detail modal

  const crops = [
    'All',
    'Apple',
    'Blueberry',
    'Cherry',
    'Corn',
    'Grape',
    'Orange',
    'Peach',
    'Pepper',
    'Potato',
    'Raspberry',
    'Soybean',
    'Squash',
    'Strawberry',
    'Tomato'
  ];

  useEffect(() => {
    fetchGuidance();
  }, [selectedCrop, search]);

  const fetchGuidance = async () => {
    setLoading(true);
    try {
      const cropFilter = selectedCrop === 'All' ? '' : selectedCrop;
      const data = await api.getGuidanceList(cropFilter, search);
      setItems(data);
    } catch (err) {
      console.error("Failed to load guidance:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8 pb-16">
      
      {/* Header */}
      <div>
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-teal-100 dark:bg-teal-950/70 text-teal-800 dark:text-teal-300 text-xs font-semibold mb-2">
          <BookOpen className="w-3.5 h-3.5" />
          <span>Curated Agronomic Knowledge Base</span>
        </div>
        <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white">
          Plant Disease Encyclopedia & Treatment Library
        </h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
          Explore comprehensive diagnostic criteria, symptoms, organic biological cures, and registered chemical fungicides 
          across all 38 plant pathologies.
        </p>
      </div>

      {/* Search & Filter Controls */}
      <div className="flex flex-col sm:flex-row gap-4">
        {/* Search Input */}
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
          <input 
            type="text" 
            placeholder="Search disease, symptoms, or remedies (e.g. Scab, Neem oil, Wilt)..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full text-xs pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
          />
        </div>

        {/* Crop Filter Dropdown */}
        <div className="flex items-center space-x-2 overflow-x-auto pb-1 sm:pb-0">
          {crops.map((c) => {
            const isSelected = (selectedCrop === '' && c === 'All') || selectedCrop === c;
            return (
              <button
                key={c}
                onClick={() => setSelectedCrop(c === 'All' ? '' : c)}
                className={`px-3 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-colors ${
                  isSelected
                    ? 'bg-emerald-600 text-white shadow-sm'
                    : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:border-emerald-400'
                }`}
              >
                {c}
              </button>
            );
          })}
        </div>
      </div>

      {/* Grid of Disease Cards */}
      {loading ? (
        <div className="flex flex-col items-center justify-center p-16 text-slate-400 space-y-3">
          <RefreshCw className="w-8 h-8 animate-spin text-emerald-500" />
          <p className="text-xs">Loading agronomic library...</p>
        </div>
      ) : items.length === 0 ? (
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-12 text-center">
          <p className="text-sm font-semibold text-slate-600 dark:text-slate-400">
            No disease records matched your search query.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map((item) => (
            <div
              key={item.disease_key}
              onClick={() => setActiveItem(item)}
              className="group p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-emerald-500/60 shadow-sm hover:shadow-lg transition-all duration-150 cursor-pointer flex flex-col justify-between"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                    {item.crop}
                  </span>
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                    item.is_healthy
                      ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                      : 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'
                  }`}>
                    {item.is_healthy ? 'Healthy' : 'Pathogen'}
                  </span>
                </div>

                <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors">
                  {item.disease}
                </h3>

                <p className="text-xs text-slate-600 dark:text-slate-400 line-clamp-3 leading-relaxed">
                  {item.summary}
                </p>

                {item.symptoms && item.symptoms.length > 0 && (
                  <div className="pt-2 border-t border-slate-100 dark:border-slate-800">
                    <span className="text-[10px] font-bold uppercase text-slate-400 block mb-1">Key Symptoms:</span>
                    <p className="text-xs text-slate-500 dark:text-slate-400 truncate">
                      • {item.symptoms[0]}
                    </p>
                  </div>
                )}
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs font-semibold text-emerald-600 dark:text-emerald-400">
                <span>View Full Treatment Protocol</span>
                <span className="group-hover:translate-x-1 transition-transform">→</span>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Detail Modal */}
      {activeItem && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 rounded-3xl max-w-2xl w-full max-h-[85vh] overflow-y-auto border border-slate-200 dark:border-slate-800 shadow-2xl p-6 sm:p-8 space-y-6 animate-fadeIn">
            
            {/* Modal Header */}
            <div className="flex items-start justify-between">
              <div>
                <span className="text-xs font-mono font-semibold px-2.5 py-1 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                  {activeItem.crop}
                </span>
                <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white mt-2">
                  {activeItem.disease}
                </h2>
              </div>
              <button
                onClick={() => setActiveItem(null)}
                className="p-2 rounded-xl text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
              {activeItem.summary}
            </p>

            {/* Symptoms */}
            {activeItem.symptoms && activeItem.symptoms.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-xs font-bold uppercase tracking-wider text-amber-700 dark:text-amber-400 flex items-center">
                  <AlertTriangle className="w-4 h-4 mr-1.5" />
                  Diagnostic Field Symptoms
                </h4>
                <ul className="space-y-1.5">
                  {activeItem.symptoms.map((s, i) => (
                    <li key={i} className="text-xs text-slate-700 dark:text-slate-300 flex items-start bg-amber-50/50 dark:bg-amber-950/20 p-2.5 rounded-xl border border-amber-100 dark:border-amber-900/30">
                      <span className="text-amber-500 font-bold mr-2">•</span>
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Organic Controls */}
            {activeItem.organic_treatments && activeItem.organic_treatments.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-xs font-bold uppercase tracking-wider text-emerald-700 dark:text-emerald-400 flex items-center">
                  <CheckCircle2 className="w-4 h-4 mr-1.5" />
                  Organic & Biological Controls
                </h4>
                <ul className="space-y-1.5">
                  {activeItem.organic_treatments.map((org, i) => (
                    <li key={i} className="text-xs text-slate-700 dark:text-slate-300 flex items-start bg-emerald-50/50 dark:bg-emerald-950/20 p-2.5 rounded-xl border border-emerald-100 dark:border-emerald-900/30">
                      <span className="text-emerald-500 font-bold mr-2">•</span>
                      <span>{org}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Chemical Controls */}
            {activeItem.chemical_treatments && activeItem.chemical_treatments.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-xs font-bold uppercase tracking-wider text-blue-700 dark:text-blue-400 flex items-center">
                  <Droplet className="w-4 h-4 mr-1.5" />
                  Chemical Interventions & Fungicides
                </h4>
                <ul className="space-y-1.5">
                  {activeItem.chemical_treatments.map((chem, i) => (
                    <li key={i} className="text-xs text-slate-700 dark:text-slate-300 flex items-start bg-slate-50 dark:bg-slate-800 p-2.5 rounded-xl border border-slate-200 dark:border-slate-700">
                      <span className="text-blue-500 font-bold mr-2">•</span>
                      <span>{chem}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Prevention */}
            {activeItem.prevention_methods && activeItem.prevention_methods.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-xs font-bold uppercase tracking-wider text-purple-700 dark:text-purple-400 flex items-center">
                  <ShieldAlert className="w-4 h-4 mr-1.5" />
                  Farm Preventive Management
                </h4>
                <ul className="space-y-1.5">
                  {activeItem.prevention_methods.map((prev, i) => (
                    <li key={i} className="text-xs text-slate-700 dark:text-slate-300 flex items-start bg-purple-50/50 dark:bg-purple-950/20 p-2.5 rounded-xl border border-purple-100 dark:border-purple-900/30">
                      <span className="text-purple-500 font-bold mr-2">•</span>
                      <span>{prev}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="pt-4 border-t border-slate-100 dark:border-slate-800 text-right">
              <button
                onClick={() => setActiveItem(null)}
                className="px-5 py-2.5 rounded-xl bg-slate-800 text-white hover:bg-slate-700 font-semibold text-xs"
              >
                Close Protocol
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
