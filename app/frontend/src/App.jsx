import { useEffect, useState } from 'react'
import StatusPill from './components/StatusPill'

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export default function App() {
  const [message, setMessage] = useState('')
  const [reply, setReply] = useState('')
  const [mode, setMode] = useState('MODE JARVIS TOTAL')
  const [health, setHealth] = useState(false)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetch(`${API_BASE}/api/health`)
      .then((res) => res.json())
      .then((data) => setHealth(data.status === 'ok'))
      .catch(() => setHealth(false))
  }, [])

  const submit = async (event) => {
    event.preventDefault()
    if (!message.trim()) return

    setLoading(true)
    try {
      const res = await fetch(`${API_BASE}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
      })
      const data = await res.json()
      setReply(data.answer)
      setMode(data.mode)
      setMessage('')
    } catch {
      setReply('Erreur de connexion API. Vérifie le backend FastAPI.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="jarvis-shell">
      <section className="hud-panel">
        <p className="kicker">SYSTÈME IA</p>
        <h1>JARVIS WEB</h1>
        <div className="status-row">
          <StatusPill label={`Backend ${health ? 'connecté' : 'hors ligne'}`} healthy={health} />
          <StatusPill label={mode} healthy />
          <StatusPill label="Sans vidéo" healthy />
        </div>
      </section>

      <section className="console-panel">
        <form onSubmit={submit} className="chat-form">
          <label htmlFor="prompt">Commande utilisateur</label>
          <textarea
            id="prompt"
            value={message}
            placeholder="Ex: Active le mode réflexion et planifie mon projet"
            onChange={(e) => setMessage(e.target.value)}
            rows={4}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Traitement...' : 'Envoyer'}
          </button>
        </form>

        <article className="response-box">
          <h2>Réponse</h2>
          <p>{reply || 'Aucune réponse pour le moment.'}</p>
        </article>
      </section>
    </main>
  )
}
