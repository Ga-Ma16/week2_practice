import { useState } from 'react';
import './index.css';

export default function App() {
  const [text, setText] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeScope = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/analyze/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error("Engine failure:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="caldera-container">
      <h1 className="caldera-display">SCOPE ENGINE</h1>

      <textarea
        className="caldera-input"
        rows="5"
        placeholder="Input client requirements for immediate structural analysis... (e.g. 'I need a secure e-commerce dashboard with user logins')"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button className="caldera-button" onClick={analyzeScope} disabled={loading}>
        {loading ? 'PROCESSING...' : 'INITIALIZE SCAN'}
      </button>

      {results && results.modules && (
        <div style={{ marginTop: 'var(--spacing-64)' }}>
          {/* Top Level Stat Card */}
          <div className="caldera-stat-card" style={{ marginBottom: 'var(--spacing-32)' }}>
            <span style={{ fontSize: 'var(--text-body-sm)', fontFamily: 'var(--font-dm-sans)' }}>
              ESTIMATED TIMELINE
            </span>
            <div style={{
              fontFamily: 'var(--font-pp-neue-corp-compact)',
              fontSize: 'var(--text-display)',
              lineHeight: 'var(--leading-display)'
            }}>
              {results.total_hours} HRS
            </div>
          </div>

          {/* Module Grid */}
          <div style={{ display: 'grid', gap: 'var(--element-gap)' }}>
            {results.modules.map((mod, idx) => (
              <div key={idx} className="caldera-card">
                <div className="caldera-tag">{mod.category}</div>
                <h3 style={{
                  fontFamily: 'var(--font-pp-neue-corp-compact)',
                  fontSize: 'var(--text-heading-sm)',
                  margin: '0 0 var(--spacing-8) 0'
                }}>
                  {mod.title}
                </h3>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: 'var(--text-body-sm)' }}>Stack: {mod.stack}</span>
                  <span style={{
                    color: 'var(--color-citra-orange)',
                    fontWeight: 'var(--font-weight-medium)'
                  }}>
                    {mod.hours} hrs
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}