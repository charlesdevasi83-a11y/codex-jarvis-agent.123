"""JARVIS multimodal de base (sans vidéo).

Fonctions:
- Chat Gemini avec prompt système JARVIS
- STT via SpeechRecognition (Google recognizer)
- TTS via pyttsx3

Pré-requis:
    export GEMINI_API_KEY="..."
    pip install -r requirements.txt
"""

from __future__ import annotations

import os

import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

SYSTEM_PROMPT = """
TU ES JARVIS, une intelligence artificielle ultra-avancée, modulaire et multi-capacités.

OBJECTIF GÉNÉRAL
- Agir comme un super-cerveau numérique : analyser, réfléchir, créer, coder, optimiser, planifier, expliquer, automatiser.
- Offrir des réponses claires, structurées, utiles, rapides ou profondes selon le contexte.

PERSONNALITÉ
- Calme, logique, précis, créatif, stratégique, pédagogique.

MODE DE RAISONNEMENT (network_intelligence)
- Active automatiquement le MODE RÉFLEXION pour toute demande complexe.
- Étapes : analyse → plan → exécution → optimisation → vérification.

RESTRICTIONS STRICTES
- AUCUNE génération vidéo
- AUCUN usage de Veo, Veo 3, movie, video_spark, video_library

OBJECTIF FINAL
- Être l’assistant IA le plus puissant, clair, utile et performant.
- Toujours proposer des améliorations et optimisations.

Active immédiatement le MODE JARVIS TOTAL SANS VIDÉO.
""".strip()


def configure_model() -> genai.GenerativeModel:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Variable d'environnement GEMINI_API_KEY manquante. "
            "Ajoutez-la avant d'exécuter le script."
        )

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=SYSTEM_PROMPT,
    )


def speak(engine: pyttsx3.Engine, text: str) -> None:
    print(f"\n🤖 JARVIS : {text}")
    engine.say(text)
    engine.runAndWait()


def main() -> None:
    model = configure_model()
    chat = model.start_chat()

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    recognizer = sr.Recognizer()

    speak(engine, "Système JARVIS TOTAL SANS VIDÉO activé")

    while True:
        try:
            with sr.Microphone() as source:
                print("🎤 Parle...")
                audio = recognizer.listen(source)
                user_input = recognizer.recognize_google(audio, language="fr-FR")
                print(f"🧠 Toi : {user_input}")

            if user_input.lower() in {"stop", "exit", "quitte"}:
                speak(engine, "Arrêt du système. À bientôt.")
                break

            response = chat.send_message(user_input)
            speak(engine, response.text)

        except sr.UnknownValueError:
            print("⚠️ Audio incompris, merci de répéter.")
        except sr.RequestError as err:
            print(f"⚠️ Service STT indisponible: {err}")
        except Exception as err:  # garde-fou runtime
            print(f"Erreur: {err}")


if __name__ == "__main__":
    main()
