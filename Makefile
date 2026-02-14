.PHONY: backend frontend dev

backend:
	cd app/backend && uvicorn main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd app/frontend && npm run dev -- --host 0.0.0.0 --port 5173

dev:
	@echo "Lancez dans 2 terminaux:"
	@echo "  make backend"
	@echo "  make frontend"
