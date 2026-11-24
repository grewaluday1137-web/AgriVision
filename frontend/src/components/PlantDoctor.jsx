import React, { useState, useEffect, useRef } from 'react';
import { 
  Upload, 
  Image as ImageIcon, 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert, 
  RefreshCw, 
  Sparkles, 
  FileText, 
  Leaf, 
  Droplet, 
  HelpCircle,
  ExternalLink,
  ChevronRight
} from 'lucide-react';
import { api } from '../api/client';

export default function PlantDoctor() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [samples, setSamples] = useState([]);
  const [loading, setLoading] = useState(false);
  const [loadingSamples, setLoadingSamples] = useState(true);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const [userNotes, setUserNotes] = useState('');
  const [activeTab, setActiveTreatmentTab] = useState('organic'); // 'organic', 'chemical', 'prevention'

  const fileInputRef = useRef(null);

  // Load sample images on mount
  useEffect(() => {
    api.getDiseaseSamples()
      .then(data => {
        setSamples(data);
        setLoadingSamples(false);
      })
      .catch(err => {
        console.error("Failed to load sample images:", err);
        setLoadingSamples(false);
      });
  }, []);

  // Handle local file selection
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
      setPrediction(null);
      setError(null);
    }
  };

  // Drag and drop handlers
  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0];
      setSelectedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
      setPrediction(null);
      setError(null);
    }
  };

  const handleDragOver = (e) => e.preventDefault();

  // Run prediction on uploaded file
  const runFilePrediction = async () => {
    if (!selectedFile) return;
    setLoading(true);
    setError(null);
    try {
      const res = await api.predictDiseaseFile(selectedFile, userNotes);
      setPrediction(res);
    } catch (err) {
      setError(err.message || 'Diagnosis failed. Please verify the image file.');
    } finally {
      setLoading(false);
    }
  };

  // Run prediction on 1-click sample image
  const runSamplePrediction = async (sample) => {
    setLoading(true);
    setError(null);
    setPrediction(null);
    setSelectedFile(null);
    setPreviewUrl(sample.image_url);

    try {
      const res = await api.predictDiseaseSample(sample.filename, userNotes);
      setPrediction(res);
    } catch (err) {
      setError(err.message || 'Diagnosis failed for sample image.');
    } finally {
      setLoading(false);
    }
  };

  const clearImage = () => {
    setSelectedFile(null);
    setPreviewUrl(null);
    setPrediction(null);
    setError(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  return (
    <div className="space-y-8 pb-16">
      
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950/70 text-emerald-800 dark:text-emerald-300 text-xs font-semibold mb-2">
            <Leaf className="w-3.5 h-3.5" />
            <span>ResNet9 PyTorch Computer Vision Engine</span>
          </div>
          <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white">
            Plant Doctor & Pathogen Classifier
          </h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            Upload an image of a crop leaf or select a sample specimen to detect 38 plant pathologies and generate agronomic prescriptions.
          </p>
        </div>

        {previewUrl && (
          <button
            onClick={clearImage}
            className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-700 transition-colors"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>Reset Image</span>
          </button>
        )}
      </div>

      {/* Main Grid: Upload & Preview on Left, Diagnosis on Right */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Column: Upload Dropzone & Sample Carousel (5 cols) */}
        <div className="lg:col-span-5 space-y-6">
          
          {/* Dropzone Card */}
          <div 
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            className={`relative rounded-2xl border-2 border-dashed transition-all duration-200 p-6 flex flex-col items-center justify-center text-center bg-white dark:bg-slate-900 ${
              previewUrl
                ? 'border-emerald-400/80 dark:border-emerald-600'
                : 'border-slate-300 dark:border-slate-700 hover:border-emerald-500/60 dark:hover:border-emerald-500/60'
            }`}
          >
            {previewUrl ? (
              <div className="w-full space-y-4">
                <div className="relative mx-auto rounded-xl overflow-hidden shadow-lg border border-slate-200 dark:border-slate-800 max-h-72 flex items-center justify-center bg-slate-950">
                  <img 
                    src={previewUrl} 
                    alt="Leaf specimen" 
                    className="max-h-72 w-auto object-contain mx-auto"
                  />
                  {loading && (
                    <div className="absolute inset-0 bg-slate-950/60 backdrop-blur-sm flex flex-col items-center justify-center text-white space-y-2">
                      <RefreshCw className="w-8 h-8 animate-spin text-emerald-400" />
                      <span className="text-xs font-medium tracking-wide">Analyzing Foliage via ResNet9...</span>
                    </div>
                  )}
                </div>

                {selectedFile && !prediction && (
                  <button
                    onClick={runFilePrediction}
                    disabled={loading}
                    className="w-full py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-bold shadow-md shadow-emerald-600/20 flex items-center justify-center space-x-2 transition-all"
                  >
                    <Sparkles className="w-4 h-4" />
                    <span>Run Diagnosis</span>
                  </button>
                )}
              </div>
            ) : (
              <div className="py-8 space-y-4 cursor-pointer" onClick={() => fileInputRef.current?.click()}>
                <div className="w-16 h-16 rounded-2xl bg-emerald-50 dark:bg-emerald-950/50 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto shadow-inner">
                  <Upload className="w-8 h-8" />
                </div>
                <div>
                  <p className="text-base font-semibold text-slate-800 dark:text-slate-200">
                    Drop your plant leaf photo here
                  </p>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                    Supports JPG, JPEG, PNG, or WebP up to 10 MB
                  </p>
                </div>
                <button
                  type="button"
                  className="px-4 py-2 rounded-lg bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-semibold text-xs border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-100 transition-colors"
                >
                  Browse Files
                </button>
              </div>
            )}

            <input 
              ref={fileInputRef}
              type="file" 
              accept="image/*" 
              onChange={handleFileChange} 
              className="hidden" 
            />
          </div>

          {/* User Notes (Optional) */}
          <div className="rounded-xl p-4 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
            <label className="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center space-x-1.5">
              <FileText className="w-3.5 h-3.5 text-slate-400" />
              <span>Agronomic Observation Notes (Optional)</span>
            </label>
            <input 
              type="text" 
              placeholder="e.g. Field plot 4B, spotted 3 days after rainstorm"
              value={userNotes}
              onChange={(e) => setUserNotes(e.target.value)}
              className="w-full text-xs px-3 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:outline-none focus:ring-1 focus:ring-emerald-500"
            />
          </div>

          {/* 1-Click Interactive Sample Carousel */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                1-Click Test Specimens ({samples.length})
              </span>
              <span className="text-[10px] text-emerald-600 dark:text-emerald-400 font-medium">
                Tap to auto-diagnose
              </span>
            </div>

            {loadingSamples ? (
              <div className="flex items-center justify-center p-4 text-xs text-slate-400">
                <RefreshCw className="w-4 h-4 animate-spin mr-2" />
                <span>Loading test specimens...</span>
              </div>
            ) : (
              <div className="grid grid-cols-3 gap-2.5 max-h-64 overflow-y-auto pr-1">
                {samples.slice(0, 15).map((sample, idx) => (
                  <button
                    key={idx}
                    onClick={() => runSamplePrediction(sample)}
                    disabled={loading}
                    className="group relative rounded-xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-slate-100 dark:bg-slate-800 hover:border-emerald-500 transition-all text-left flex flex-col focus:outline-none"
                  >
                    <div className="w-full h-16 bg-slate-900 overflow-hidden">
                      <img 
                        src={sample.image_url} 
                        alt={sample.display_name} 
                        className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-200"
                        loading="lazy"
                      />
                    </div>
                    <div className="p-1.5">
                      <p className="text-[10px] font-semibold text-slate-800 dark:text-slate-200 truncate group-hover:text-emerald-600 dark:group-hover:text-emerald-400">
                        {sample.display_name}
                      </p>
                    </div>
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Diagnostic & Treatment Plan (7 cols) */}
        <div className="lg:col-span-7 space-y-6">
          
          {error && (
            <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 text-rose-800 dark:text-rose-200 text-sm flex items-start space-x-3">
              <AlertTriangle className="w-5 h-5 flex-shrink-0 text-rose-600 dark:text-rose-400 mt-0.5" />
              <div>
                <p className="font-semibold">Inference Error</p>
                <p className="text-xs mt-1">{error}</p>
              </div>
            </div>
          )}

          {prediction ? (
            <div className="space-y-6 animate-fadeIn">
              
              {/* Primary Diagnostic Banner */}
              <div className={`rounded-2xl p-6 border shadow-md transition-all ${
                prediction.is_healthy
                  ? 'bg-gradient-to-br from-emerald-50 via-teal-50 to-white dark:from-emerald-950/60 dark:via-slate-900 dark:to-slate-900 border-emerald-300 dark:border-emerald-800'
                  : 'bg-gradient-to-br from-amber-50 via-orange-50 to-white dark:from-amber-950/60 dark:via-slate-900 dark:to-slate-900 border-amber-300 dark:border-amber-800'
              }`}>
                <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
                  <div>
                    <div className="flex items-center space-x-2">
                      <span className={`inline-flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold ${
                        prediction.is_healthy
                          ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/80 dark:text-emerald-200'
                          : 'bg-rose-100 text-rose-800 dark:bg-rose-900/80 dark:text-rose-200'
                      }`}>
                        {prediction.is_healthy ? (
                          <CheckCircle2 className="w-3.5 h-3.5" />
                        ) : (
                          <AlertTriangle className="w-3.5 h-3.5" />
                        )}
                        <span>{prediction.is_healthy ? 'Foliage Healthy' : 'Pathogen Detected'}</span>
                      </span>

                      <span className="text-xs font-mono px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                        {prediction.crop}
                      </span>
                    </div>

                    <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-3">
                      {prediction.disease}
                    </h2>

                    <p className="text-sm text-slate-600 dark:text-slate-300 mt-2 leading-relaxed">
                      {prediction.guidance?.summary || 'Pathology evaluation generated from deep neural network layer activations.'}
                    </p>
                  </div>

                  {/* Confidence Score Gauge */}
                  <div className="text-right flex-shrink-0 bg-white/80 dark:bg-slate-800/80 p-3.5 rounded-xl border border-slate-200/60 dark:border-slate-700">
                    <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 block uppercase">Confidence</span>
                    <span className="text-3xl font-black text-emerald-600 dark:text-emerald-400">
                      {prediction.confidence_pct}%
                    </span>
                    <div className="w-24 h-2 bg-slate-100 dark:bg-slate-700 rounded-full mt-2 overflow-hidden">
                      <div 
                        className="h-full bg-emerald-500 rounded-full"
                        style={{ width: `${Math.min(100, prediction.confidence_pct)}%` }}
                      ></div>
                    </div>
                  </div>
                </div>

                {/* Top-3 Candidates Breakdown */}
                {prediction.top_predictions && prediction.top_predictions.length > 1 && (
                  <div className="mt-6 pt-4 border-t border-slate-200/80 dark:border-slate-800/80">
                    <span className="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 block mb-2">
                      Multi-Candidate Probability Distribution:
                    </span>
                    <div className="space-y-2">
                      {prediction.top_predictions.map((cand, i) => (
                        <div key={i} className="flex items-center justify-between text-xs">
                          <span className="text-slate-700 dark:text-slate-300 font-medium">
                            {cand.crop} — {cand.disease}
                          </span>
                          <div className="flex items-center space-x-2">
                            <div className="w-24 h-1.5 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                              <div 
                                className="h-full bg-emerald-500 rounded-full"
                                style={{ width: `${cand.confidence_pct}%` }}
                              ></div>
                            </div>
                            <span className="font-mono font-bold text-slate-600 dark:text-slate-400 w-12 text-right">
                              {cand.confidence_pct}%
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Agronomic Treatment Manual (Drawer) */}
              {prediction.guidance && (
                <div className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm overflow-hidden">
                  
                  {/* Treatment Navigation Tabs */}
                  <div className="flex border-b border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/40">
                    <button
                      onClick={() => setActiveTreatmentTab('organic')}
                      className={`flex-1 py-3 px-4 text-xs font-bold text-center border-b-2 transition-colors ${
                        activeTab === 'organic'
                          ? 'border-emerald-500 text-emerald-600 dark:text-emerald-400 bg-white dark:bg-slate-900'
                          : 'border-transparent text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      🌿 Organic & Bio Controls
                    </button>
                    <button
                      onClick={() => setActiveTreatmentTab('chemical')}
                      className={`flex-1 py-3 px-4 text-xs font-bold text-center border-b-2 transition-colors ${
                        activeTab === 'chemical'
                          ? 'border-emerald-500 text-emerald-600 dark:text-emerald-400 bg-white dark:bg-slate-900'
                          : 'border-transparent text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      🧪 Chemical Treatments
                    </button>
                    <button
                      onClick={() => setActiveTreatmentTab('prevention')}
                      className={`flex-1 py-3 px-4 text-xs font-bold text-center border-b-2 transition-colors ${
                        activeTab === 'prevention'
                          ? 'border-emerald-500 text-emerald-600 dark:text-emerald-400 bg-white dark:bg-slate-900'
                          : 'border-transparent text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      🛡️ Farm Prevention
                    </button>
                  </div>

                  {/* Tab Contents */}
                  <div className="p-6">
                    {/* Symptoms Callout */}
                    {prediction.guidance.symptoms && prediction.guidance.symptoms.length > 0 && (
                      <div className="mb-6 p-4 rounded-xl bg-amber-50/50 dark:bg-amber-950/20 border border-amber-200/50 dark:border-amber-900/30">
                        <h4 className="text-xs font-bold uppercase tracking-wider text-amber-800 dark:text-amber-300 mb-2 flex items-center">
                          <AlertTriangle className="w-3.5 h-3.5 mr-1.5" />
                          Diagnostic Symptoms Checklist
                        </h4>
                        <ul className="space-y-1">
                          {prediction.guidance.symptoms.map((sym, i) => (
                            <li key={i} className="text-xs text-slate-700 dark:text-slate-300 flex items-start">
                              <span className="text-amber-500 mr-2 font-bold">•</span>
                              <span>{sym}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Active Tab View */}
                    {activeTab === 'organic' && (
                      <div className="space-y-3">
                        <h4 className="text-sm font-bold text-slate-900 dark:text-white">
                          Organic & Biological Interventions:
                        </h4>
                        <ul className="space-y-2">
                          {(prediction.guidance.organic_treatments || prediction.guidance.organic_controls || []).map((org, i) => (
                            <li key={i} className="flex items-start text-xs text-slate-700 dark:text-slate-300 bg-emerald-50/40 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-100 dark:border-emerald-900/40">
                              <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 mr-2 flex-shrink-0 mt-0.5" />
                              <span className="leading-relaxed">{org}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {activeTab === 'chemical' && (
                      <div className="space-y-3">
                        <h4 className="text-sm font-bold text-slate-900 dark:text-white">
                          Registered Chemical Fungicides / Remediation:
                        </h4>
                        <ul className="space-y-2">
                          {(prediction.guidance.chemical_treatments || prediction.guidance.chemical_controls || []).map((chem, i) => (
                            <li key={i} className="flex items-start text-xs text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-800/50 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                              <Droplet className="w-4 h-4 text-blue-500 mr-2 flex-shrink-0 mt-0.5" />
                              <span className="leading-relaxed">{chem}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {activeTab === 'prevention' && (
                      <div className="space-y-3">
                        <h4 className="text-sm font-bold text-slate-900 dark:text-white">
                          Long-Term Cultural & Preventive Agronomic Measures:
                        </h4>
                        <ul className="space-y-2">
                          {(prediction.guidance.prevention_methods || prediction.guidance.prevention_measures || []).map((prev, i) => (
                            <li key={i} className="flex items-start text-xs text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-800/50 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                              <ShieldAlert className="w-4 h-4 text-amber-500 mr-2 flex-shrink-0 mt-0.5" />
                              <span className="leading-relaxed">{prev}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          ) : (
            /* Empty State Guidance */
            <div className="h-full min-h-[380px] rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-8 flex flex-col items-center justify-center text-center space-y-4 shadow-sm">
              <div className="w-16 h-16 rounded-2xl bg-emerald-50 dark:bg-emerald-950/50 text-emerald-600 dark:text-emerald-400 flex items-center justify-center">
                <Leaf className="w-8 h-8" />
              </div>
              <div className="max-w-md">
                <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                  Awaiting Leaf Specimen
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                  Upload an image from your device or select any of the 1-click test specimens on the left. 
                  The ResNet9 model will evaluate cellular leaf patterns and output actionable agronomic solutions.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
