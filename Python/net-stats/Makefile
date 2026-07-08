.DEFAULT_GOAL := help
.PHONY: help install run test lint format clean

UV := uv

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Sync dependencies (incl. dev group)
	$(UV) sync

run: ## Run the app
	$(UV) run net-stats

test: ## Run tests
	$(UV) run pytest -v

lint: ## Lint with ruff
	$(UV) run ruff check src tests

format: ## Format with ruff
	$(UV) run ruff format src tests

clean: ## Remove venv, caches, build artifacts
	rm -rf .venv .pytest_cache .ruff_cache dist
	find . -type d -name __pycache__ -exec rm -rf {} +
