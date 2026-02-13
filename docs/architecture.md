# Architecture Technique Recommandée — JARVIS Sans Vidéo

## Frontend

- **Stack**: React / Next.js
- **Fonctions UI**:
  - Chat temps réel
  - Bouton micro (input vocal)
  - Upload image/document
  - Affichage réponses structurées (résumés, plans, checklists)

## Backend

- **Option 1**: Python FastAPI
- **Option 2**: Node.js (Express / Nest)
- **Responsabilités**:
  - Orchestration des appels IA
  - Gestion du contexte conversationnel (mémoire)
  - Auth/API keys/quotas
  - Journalisation et monitoring

## Services IA à intégrer

1. **Gemini API**
   - Chat principal (raisonnement, génération de texte, assistance code)
2. **Speech-to-Text (STT)**
   - Transcription voix → texte
3. **Text-to-Speech (TTS)**
   - Restitution vocale des réponses
4. **Image generation / image edit**
   - Génération et édition d’images
5. **OCR / document analysis**
   - Extraction et synthèse d’informations depuis documents
6. **Google Search API**
   - Recherche web en temps réel
7. **Google Maps API**
   - Lieux, itinéraires, distance, points d’intérêt

## Modules fonctionnels actifs

- 🎨 Génération & édition d’images
- 🧠 OCR + analyse de documents
- 🌐 Recherche web
- 🗺️ Google Maps
- 🗣️ STT + TTS

## Contraintes

- **Aucune génération vidéo**.
- Interdiction explicite d’utiliser : `Veo`, `Veo 3`, `video_spark`, `movie`, `video_library`.

## Commandes d’activation (UX)

- `MODE JARVIS TOTAL`
- `MODE RÉFLEXION`
- `MODE IMAGE CINÉMA`
