.PHONY: dev test lint

dev:
	export FLASK_APP=app.github_webhook && flask run --reload --host=0.0.0.0 --port=8000

test:
	PYTHONPATH=. pytest

lint:
	black . && isort . 