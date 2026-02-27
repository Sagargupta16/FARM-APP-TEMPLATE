.PHONY: help install dev build test lint docker-up docker-down docker-rebuild

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies (backend + frontend)
	pip install -r requirements.txt
	cd client && npm install

dev: ## Start backend dev server
	uvicorn main:app --reload

dev-frontend: ## Start frontend dev server
	cd client && npm run dev

build: ## Build frontend for production
	cd client && npm run build

test: ## Run backend tests
	python -m pytest tests/

lint: ## Run ruff linter
	ruff check .

lint-fix: ## Run ruff linter with auto-fix
	ruff check --fix .

docker-up: ## Start all services with Docker Compose
	docker compose up -d

docker-down: ## Stop all Docker Compose services
	docker compose down

docker-rebuild: ## Rebuild and start all services
	docker compose up --build -d

docker-logs: ## Follow Docker Compose logs
	docker compose logs -f
