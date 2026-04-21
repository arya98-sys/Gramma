import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleCorrect = async () => {
    if (!input || input.length < 3) return;
    setLoading(true);
    try {
      const response = await axios.post('https://arya98-gramma.hf.space', { text: input });
      setOutput(response.data.corrected);
    } catch (error) {
      console.error("Backend Error");
    }
    setLoading(false);
  };

  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      {/* Dark Silk Header */}
      <header className="text-center mb-16 space-y-2">
        <h1 className="text-5xl font-black tracking-tighter text-white glow-text">
          GRAMMA<span className="text-blue-500">AI</span>
        </h1>
        <p className="text-slate-400 font-light tracking-widest uppercase text-xs">
          Neural Writing Architecture
        </p>
      </header>

      <main className="space-y-8">
        {/* Editor Container */}
        <div className="silk-card rounded-3xl p-2 transition-all duration-500 hover:border-blue-500/30">
          <textarea
            className="w-full h-64 p-8 bg-transparent border-none focus:ring-0 text-xl text-slate-200 placeholder-slate-600 resize-none italic font-light"
            placeholder="Enter text to refine..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <div className="flex items-center justify-between px-8 py-6 border-t border-white/5 bg-white/[0.01]">
            <div className="flex gap-4">
               <span className="text-xs text-slate-500 font-mono uppercase">{input.split(' ').filter(x => x).length} words</span>
            </div>
            <button
              onClick={handleCorrect}
              disabled={loading}
              className="relative group overflow-hidden bg-white text-black px-10 py-3 rounded-full font-bold transition-all hover:scale-105 active:scale-95 disabled:opacity-50"
            >
              <span className="relative z-10">{loading ? "PROCESSING..." : "REFINE TEXT"}</span>
              <div className="absolute inset-0 bg-blue-500 translate-y-[100%] group-hover:translate-y-0 transition-transform duration-300"></div>
            </button>
          </div>
        </div>

        {/* AI Output Result */}
        {output && (
          <div className="silk-card rounded-3xl p-10 animate-in fade-in zoom-in duration-700">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
              <h3 className="text-xs font-black text-blue-500 uppercase tracking-[0.2em]">Refined Result</h3>
            </div>
            <p className="text-2xl text-white leading-relaxed font-serif italic">
              "{output}"
            </p>
            <button 
               onClick={() => navigator.clipboard.writeText(output)}
               className="mt-8 text-xs text-slate-500 hover:text-white transition-colors border-b border-slate-800 pb-1"
            >
              COPY TO ARCHIVE
            </button>
          </div>
        )}
      </main>

      <footer className="mt-24 text-center">
        <p className="text-[10px] text-slate-600 tracking-[0.5em] uppercase">
          CS Department • AI Integration Project 2026
        </p>
      </footer>
    </div>
  );
}

export default App;