# JARVIS Web App (React + FastAPI)

Application web complète avec :
- Frontend **React (Vite)** moderne
- UI futuriste style **JARVIS**
- Backend **FastAPI**
- Développement local avec **hot reload** (frontend + backend)

## Structure

```text
app/
  backend/
    main.py
    requirements.txt
  frontend/
    index.html
    package.json
    vite.config.js
    src/
      App.jsx
      components/StatusPill.jsx
      styles/jarvis.css
Makefile
```

## Prérequis

- Python 3.10+
- Node.js 18+
- npm

## Installation backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r app/backend/requirements.txt
```

## Installation frontend

```bash
cd app/frontend
npm install
cd ../..
```

## Lancement local (hot reload)

Ouvre **2 terminaux**.

Terminal 1 (FastAPI avec reload) :

```bash
make backend
```

Terminal 2 (React Vite avec reload) :

```bash
make frontend
```

Ensuite ouvre :
- Frontend : http://localhost:5173
- API : http://localhost:8000/api/health

## Développement temps réel

- Toute modification dans `app/frontend/src/*` est rechargée instantanément dans le navigateur.
- Toute modification dans `app/backend/main.py` redémarre automatiquement l’API grâce à `uvicorn --reload`.

## Endpoints backend

- `GET /api/health` : état du service.
- `POST /api/chat` : endpoint de chat simple pour piloter des modes JARVIS.

Exemple payload :

```json
{
  "message": "Active le mode réflexion"
}
```

## Contraintes

- Cette base est orientée **JARVIS sans vidéo**.
- Aucune fonctionnalité vidéo n’est implémentée.
