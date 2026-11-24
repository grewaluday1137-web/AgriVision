import React, { useState, useEffect } from 'react';
import { 
  History, 
  Trash2, 
  Download, 
  RefreshCw, 
  Stethoscope, 
  Compass, 
  TrendingUp, 
  Clock, 
  Search,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';
import { api } from '../api/client';

export default function HistoryView() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedModule, setSelectedModule] = useState('');
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetchHistory();
  }, [selectedModule]);

  const fetchHistory = async () => {
    setLoading(true);
    try {
      const data = await api.getHistory(selectedModule);
      setHistory(data);
    } catch (err) {
      console.error("Failed to load history:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteItem = async (id) => {
    try {
      await api.deleteHistoryItem(id);
      setHistory(prev => prev.filter(item => item.id !== id));
    } catch (err) {
      alert("Failed to delete record: " + err.message);
    }
  };

  const handleClearAll = async () => {
    if (!window.confirm("Are you sure you want to clear your prediction history?")) return;
    try {
      await api.clearHistory(selectedModule);
      setHistory([]);
    } catch (err) {
      alert("Failed to clear history: " + err.message);
    }
  };

  const exportToJson = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(history, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `agrivision_history_${new Date().toISOString().split('T')[0]}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  };

  const getModuleBadge = (module) => {
    switch (module) {
      case 'disease':
        return { label: 'Plant Doctor', icon: Stethoscope, color: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300' };
      case 'crop':
        return { label: 'Crop Advisor', icon: Compass, color: 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300' };
      case 'yield':
        return { label: 'Yield Forecaster', icon: TrendingUp, color: 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300' };
      default:
        return { label: module, icon: Clock, color: 'bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-300' };
    }
  };

  const filteredHistory = history.filter(item => {
    if (!search) return true;
    const s = search.toLowerCase();
    return (
      item.prediction_result?.toLowerCase().includes(s) ||
      item.input_summary?.toLowerCase().includes(s) ||
      item.module?.toLowerCase().includes(s)
    );
  });

  return (
    <div className="space-y-8 pb-16">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-300 text-xs font-semibold mb-2">
            <History className="w-3.5 h-3.5" />
            <span>SQLite Local Audit Log</span>
          </div>
          <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white">
            Prediction History & Records
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Review previous leaf disease diagnoses, soil recommendations, and yield forecasts.
          </p>
        </div>

        {/* Action Buttons */}
        <div className="flex items-center space-x-2">
          {history.length > 0 && (
            <>
              <button
                onClick={exportToJson}
                className="inline-flex items-center space-x-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors shadow-sm"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Export JSON</span>
              </button>

              <button
                onClick={handleClearAll}
                className="inline-flex items-center space-x-1.5 px-3 py-2 rounded-xl text-xs font-semibold text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 hover:bg-rose-100 transition-colors"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Clear All</span>
              </button>
            </>
          )}
        </div>
      </div>

      {/* Module Filters & Search */}
      <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">
        
        {/* Module Segmented Buttons */}
        <div className="flex space-x-2 w-full sm:w-auto overflow-x-auto pb-1 sm:pb-0">
          {[
            { id: '', label: 'All Modules' },
            { id: 'disease', label: 'Plant Doctor' },
            { id: 'crop', label: 'Crop Advisor' },
            { id: 'yield', label: 'Yield Forecaster' }
          ].map((m) => (
            <button
              key={m.id}
              onClick={() => setSelectedModule(m.id)}
              className={`px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-colors ${
                selectedModule === m.id
                  ? 'bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-sm'
                  : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-800 hover:border-slate-400'
              }`}
            >
              {m.label}
            </button>
          ))}
        </div>

        {/* Search */}
        <div className="relative w-full sm:w-72">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          <input 
            type="text" 
            placeholder="Search records..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full text-xs pl-9 pr-3 py-2 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
          />
        </div>
      </div>

      {/* History Items List */}
      {loading ? (
        <div className="flex flex-col items-center justify-center p-16 text-slate-400 space-y-3">
          <RefreshCw className="w-8 h-8 animate-spin text-slate-400" />
          <p className="text-xs">Loading records...</p>
        </div>
      ) : filteredHistory.length === 0 ? (
        <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-12 text-center space-y-3">
          <History className="w-10 h-10 text-slate-300 dark:text-slate-700 mx-auto" />
          <p className="text-sm font-semibold text-slate-700 dark:text-slate-300">
            No prediction history records found.
          </p>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Run a disease diagnosis, crop recommendation, or yield forecast to generate history logs.
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {filteredHistory.map((item) => {
            const badge = getModuleBadge(item.module);
            const Icon = badge.icon;
            const dateStr = new Date(item.created_at).toLocaleString();

            return (
              <div
                key={item.id}
                className="p-4 sm:p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-md transition-shadow flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
              >
                <div className="flex items-start space-x-3.5">
                  <div className="p-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 flex-shrink-0 mt-0.5">
                    <Icon className="w-5 h-5" />
                  </div>
                  <div className="space-y-1">
                    <div className="flex items-center space-x-2">
                      <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${badge.color}`}>
                        {badge.label}
                      </span>
                      <span className="text-[11px] text-slate-400 flex items-center">
                        <Clock className="w-3 h-3 mr-1" />
                        {dateStr}
                      </span>
                    </div>

                    <h4 className="text-base font-bold text-slate-900 dark:text-white">
                      {item.prediction_result}
                    </h4>

                    <p className="text-xs text-slate-500 dark:text-slate-400 font-mono">
                      {item.input_summary}
                    </p>
                  </div>
                </div>

                <div className="flex items-center justify-between sm:justify-end space-x-4 pt-2 sm:pt-0 border-t sm:border-t-0 border-slate-100 dark:border-slate-800">
                  {item.confidence !== null && item.confidence !== undefined && (
                    <div className="text-right">
                      <span className="text-[10px] text-slate-400 font-bold uppercase block">Confidence</span>
                      <span className="text-sm font-bold text-emerald-600 dark:text-emerald-400">
                        {Math.round(item.confidence * 100)}%
                      </span>
                    </div>
                  )}

                  <button
                    onClick={() => handleDeleteItem(item.id)}
                    className="p-2 rounded-lg text-slate-400 hover:text-rose-500 hover:bg-rose-50 dark:hover:bg-rose-950/40 transition-colors"
                    title="Delete Record"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
