from __future__ import annotations

from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Jarvis Web API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    mode: str
    timestamp: str


@app.get("/api/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "jarvis-backend"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    normalized = payload.message.strip().lower()
    if any(key in normalized for key in {"mode réflexion", "mode reflexion"}):
        mode = "MODE RÉFLEXION"
        answer = (
            "Mode Réflexion activé. Je vais répondre avec le flux : "
            "analyse → plan → exécution → optimisation → vérification."
        )
    elif "mode image" in normalized:
        mode = "MODE IMAGE CINÉMA"
        answer = (
            "Mode Image Cinéma activé. Donne-moi le sujet et je propose un prompt "
            "cinématographique détaillé (caméra, lumière, composition, rendu)."
        )
    else:
        mode = "MODE JARVIS TOTAL"
        answer = (
            "Reçu. Backend FastAPI opérationnel en temps réel. "
            f"Message traité: {payload.message}"
        )

    return ChatResponse(
        answer=answer,
        mode=mode,
        timestamp=datetime.utcnow().isoformat() + "Z",
    )
