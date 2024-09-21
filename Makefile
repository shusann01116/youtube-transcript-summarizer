setup: requirements.txt .env
	pip install -r requirements.txt

.env:
	@cp .env.sample .env

.PHONY: run
run:
	@python main.py

.PHONY: fmt
fmt:
	@python -m ruff format

.PHONY: lint
lint:
	@python -m ruff check

.PHONY: clean
clean:
	rm -rf __pycache__ .ruff_cache
