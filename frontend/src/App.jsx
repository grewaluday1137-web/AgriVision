import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import HomeHero from './components/HomeHero';
import PlantDoctor from './components/PlantDoctor';
import CropAdvisor from './components/CropAdvisor';
import YieldForecaster from './components/YieldForecaster';
import Encyclopedia from './components/Encyclopedia';
import HistoryView from './components/HistoryView';

export default function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem('agrivision_theme') === 'dark';
  });

  // Sync dark class on <html>
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('agrivision_theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('agrivision_theme', 'light');
    }
  }, [darkMode]);

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 transition-colors duration-200">
      
      {/* Navigation Header */}
      <Navbar 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        darkMode={darkMode} 
        setDarkMode={setDarkMode} 
      />

      {/* Main Content Area */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
        {activeTab === 'home' && <HomeHero setActiveTab={setActiveTab} />}
        {activeTab === 'disease' && <PlantDoctor />}
        {activeTab === 'crop' && <CropAdvisor />}
        {activeTab === 'yield' && <YieldForecaster />}
        {activeTab === 'encyclopedia' && <Encyclopedia />}
        {activeTab === 'history' && <HistoryView />}
      </main>

      {/* Footer */}
      <footer className="mt-20 border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 py-8 text-xs text-slate-500 dark:text-slate-400">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center space-x-2">
            <span className="font-bold text-slate-800 dark:text-slate-200">AgriVision AI</span>
            <span>•</span>
            <span>Intelligent Agriculture & Crop Health Platform</span>
          </div>
          <div>
            <span>Powered by PyTorch ResNet9 • XGBoost • Scikit-Learn Bagging • FastAPI • React</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
