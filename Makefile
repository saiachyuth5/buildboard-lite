.PHONY: dev test

dev:
	FLASK_APP=app.github_webhook flask run --host=0.0.0.0 --port=5000

test:
	pytest -q 