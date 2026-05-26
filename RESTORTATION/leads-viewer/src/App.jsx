import { useState, useEffect } from 'react';
import Papa from 'papaparse';
import { 
  Search, 
  Phone, 
  MapPin, 
  Star, 
  Clock, 
  Briefcase, 
  Save,
  MessageSquare,
  Users
} from 'lucide-react';

function App() {
  const [leads, setLeads] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedLead, setSelectedLead] = useState(null);
  const [notes, setNotes] = useState({});
  const [currentNote, setCurrentNote] = useState('');

  // Load notes from local storage on mount
  useEffect(() => {
    const savedNotes = localStorage.getItem('hvac_cold_call_notes');
    if (savedNotes) {
      try {
        setNotes(JSON.parse(savedNotes));
      } catch (e) {
        console.error('Failed to parse notes from local storage', e);
      }
    }

    // Fetch and parse CSV
    fetch('/leads.csv')
      .then(response => response.text())
      .then(csvText => {
        Papa.parse(csvText, {
          header: true,
          skipEmptyLines: true,
          complete: (results) => {
            setLeads(results.data);
          }
        });
      })
      .catch(err => console.error('Error loading CSV:', err));
  }, []);

  // Filter leads based on search
  const filteredLeads = leads.filter(lead => {
    if (!searchTerm) return true;
    const term = searchTerm.toLowerCase();
    return (
      (lead.Name && lead.Name.toLowerCase().includes(term)) ||
      (lead.City && lead.City.toLowerCase().includes(term)) ||
      (lead.Phone && lead.Phone.toLowerCase().includes(term))
    );
  });

  const handleSelectLead = (lead) => {
    setSelectedLead(lead);
    setCurrentNote(notes[lead.Name] || '');
  };

  const handleSaveNote = () => {
    if (!selectedLead) return;
    
    const updatedNotes = {
      ...notes,
      [selectedLead.Name]: currentNote
    };
    
    setNotes(updatedNotes);
    localStorage.setItem('hvac_cold_call_notes', JSON.stringify(updatedNotes));
    
    // Optional: show some temporary success indication (we just rely on the button for now)
  };

  return (
    <div className="app-container">
      {/* Sidebar */}
      <aside className="glass-panel sidebar animate-fade-in">
        <div className="sidebar-header">
          <h2>Open Leads</h2>
          <div style={{ position: 'relative' }}>
            <Search size={18} style={{ position: 'absolute', top: '1.8rem', left: '1rem', color: 'var(--text-secondary)' }} />
            <input 
              type="text" 
              className="search-input" 
              placeholder="Search by name, city, or phone..." 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{ paddingLeft: '2.5rem' }}
            />
          </div>
        </div>
        
        <div className="leads-list">
          {filteredLeads.map((lead, idx) => {
            const hasNote = notes[lead.Name] && notes[lead.Name].trim().length > 0;
            return (
              <div 
                key={`${lead.Name}-${idx}`}
                className={`lead-item ${selectedLead?.Name === lead.Name ? 'active' : ''}`}
                onClick={() => handleSelectLead(lead)}
              >
                <div className="lead-name">
                  {lead.Name || 'Unknown Name'}
                  <div className={`lead-status-indicator ${hasNote ? 'has-note' : ''}`} title={hasNote ? 'Note saved' : 'No notes'} />
                </div>
                <div className="lead-meta">
                  {lead.City && lead.State ? `${lead.City}, ${lead.State}` : 'Location unavailable'}
                </div>
              </div>
            );
          })}
          {filteredLeads.length === 0 && (
            <div style={{ textAlign: 'center', color: 'var(--text-secondary)', padding: '2rem 0' }}>
              No leads found.
            </div>
          )}
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="glass-panel main-content animate-fade-in" style={{ animationDelay: '0.1s' }}>
        {!selectedLead ? (
          <div className="empty-state">
            <Users size={64} />
            <h2>Select a Lead</h2>
            <p>Click on a lead from the sidebar to view details and add cold calling notes.</p>
          </div>
        ) : (
          <>
            <div className="detail-header">
              <div>
                <h1 className="detail-title">{selectedLead.Name || 'Unknown Business'}</h1>
                <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
                  {selectedLead['Business Type'] && (
                    <span className="badge">
                      <Briefcase size={14} style={{ marginRight: '0.25rem' }} />
                      {selectedLead['Business Type']}
                    </span>
                  )}
                  {selectedLead.Rating && (
                    <span className="badge" style={{ background: 'rgba(245, 158, 11, 0.1)', color: '#fbbf24', borderColor: 'rgba(245, 158, 11, 0.2)' }}>
                      <Star size={14} style={{ marginRight: '0.25rem' }} fill="currentColor" />
                      {selectedLead.Rating} Rating
                    </span>
                  )}
                </div>
              </div>
            </div>

            <div className="detail-body">
              <div className="info-group">
                <div className="info-item">
                  <div className="info-icon">
                    <Phone size={20} />
                  </div>
                  <div className="info-content">
                    <label>Phone Number</label>
                    <p>
                      {selectedLead.Phone ? (
                        <a href={`tel:${selectedLead.Phone.replace(/[^0-9+]/g, '')}`}>{selectedLead.Phone}</a>
                      ) : 'N/A'}
                    </p>
                  </div>
                </div>

                <div className="info-item">
                  <div className="info-icon">
                    <MapPin size={20} />
                  </div>
                  <div className="info-content">
                    <label>Address</label>
                    <p>{selectedLead.Address || 'N/A'}</p>
                    {selectedLead['Google Maps Link'] && (
                      <a href={selectedLead['Google Maps Link']} target="_blank" rel="noopener noreferrer" style={{ fontSize: '0.875rem', display: 'inline-block', marginTop: '0.25rem' }}>
                        View on Google Maps →
                      </a>
                    )}
                  </div>
                </div>

                <div className="info-item">
                  <div className="info-icon">
                    <Clock size={20} />
                  </div>
                  <div className="info-content">
                    <label>Hours</label>
                    <p>{selectedLead['Sunday Hours'] || 'N/A'}</p>
                  </div>
                </div>
              </div>

              <div className="notes-section glass-panel" style={{ padding: '1.5rem', background: 'rgba(0,0,0,0.1)' }}>
                <div className="notes-header">
                  <MessageSquare size={20} color="var(--accent-color)" />
                  Cold Calling Notes
                </div>
                <textarea 
                  className="notes-textarea"
                  placeholder="Enter call notes, decision makers, follow-up dates, etc. here..."
                  value={currentNote}
                  onChange={(e) => setCurrentNote(e.target.value)}
                />
                <button className="save-btn" onClick={handleSaveNote}>
                  <Save size={18} />
                  Save Notes
                </button>
              </div>
            </div>
          </>
        )}
      </main>
    </div>
  );
}

export default App;
