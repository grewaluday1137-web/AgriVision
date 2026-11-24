const API_BASE = '/api';

/**
 * Common fetch helper with error handling
 */
async function fetchJson(endpoint, options = {}) {
  const res = await fetch(`${API_BASE}${endpoint}`, options);
  if (!res.ok) {
    let errorDetail = res.statusText;
    try {
      const errorJson = await res.json();
      errorDetail = errorJson.detail || errorJson.message || JSON.stringify(errorJson);
    } catch {
      // ignore
    }
    throw new Error(errorDetail || `Request failed with status ${res.status}`);
  }
  return res.json();
}

export const api = {
  // System Health
  getHealth: () => fetchJson('/health'),

  // Plant Doctor (Disease Diagnosis)
  getDiseaseSamples: () => fetchJson('/disease/samples'),
  
  predictDiseaseFile: async (file, notes = '') => {
    const formData = new FormData();
    formData.append('file', file);
    if (notes) formData.append('notes', notes);
    return fetchJson('/disease/predict', {
      method: 'POST',
      body: formData,
    });
  },

  predictDiseaseSample: async (filename, notes = '') => {
    const formData = new FormData();
    formData.append('filename', filename);
    if (notes) formData.append('notes', notes);
    return fetchJson('/disease/predict-sample', {
      method: 'POST',
      body: formData,
    });
  },

  // Crop Advisor (Recommendation)
  getCropPresets: () => fetchJson('/crop/presets'),
  
  recommendCrop: (params) => fetchJson('/crop/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  }),

  // Yield Forecaster
  getYieldManifest: () => fetchJson('/yield/manifest'),
  
  predictYield: (params) => fetchJson('/yield/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  }),

  // Agronomic Encyclopedia
  getGuidanceList: (crop = '', search = '') => {
    const params = new URLSearchParams();
    if (crop) params.append('crop', crop);
    if (search) params.append('search', search);
    const qs = params.toString();
    return fetchJson(`/guidance${qs ? `?${qs}` : ''}`);
  },

  getGuidanceDetail: (diseaseKey) => fetchJson(`/guidance/${encodeURIComponent(diseaseKey)}`),

  // Prediction History
  getHistory: (module = '', limit = 50) => {
    const params = new URLSearchParams();
    if (module) params.append('module', module);
    params.append('limit', limit);
    return fetchJson(`/history?${params.toString()}`);
  },

  deleteHistoryItem: (id) => fetchJson(`/history/${id}`, { method: 'DELETE' }),
  clearHistory: (module = '') => fetchJson(`/history${module ? `?module=${module}` : ''}`, { method: 'DELETE' }),
};
