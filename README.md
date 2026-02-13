# JARVIS IA Total (Sans Vidéo)

Ce dépôt fournit une base prête à l’emploi pour un assistant **JARVIS multimodal** (texte, audio, image, OCR, recherche, maps), avec une consigne stricte : **aucune génération vidéo**.

## Contenu

- `prompts/jarvis_system_prompt.fr.md` : méga prompt système en français.
- `docs/architecture.md` : architecture technique recommandée (frontend/backend/services).
- `python/jarvis_multimodal_no_video.py` : script Python de base (chat + voix + STT/TTS).
- `requirements.txt` : dépendances Python.

## Installation rapide

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Définissez votre clé API Gemini :

```bash
export GEMINI_API_KEY="VOTRE_CLE_API"
```

## Lancer JARVIS (CLI vocale)

```bash
python python/jarvis_multimodal_no_video.py
```

## Notes importantes

- Le script inclut **STT/TTS local** et interaction de chat Gemini.
- Les modules de recherche web/maps/édition d’image sont décrits dans l’architecture et peuvent être branchés côté backend selon votre stack.
- Les fonctions vidéo (Veo, Veo 3, `video_spark`, `movie`, `video_library`) sont explicitement exclues.
