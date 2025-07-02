# BuildBoard-Lite

**BuildBoard-Lite** is an open-source GitHub App bot that:
- Listens for `issues.labeled:ai-fix`
- Checks out the repo in a Docker sandbox
- Asks an LLM to patch ≤10 files / ≤400 LOC
- Opens/updates a PR until CI is green
- Escalates with label `needs-human` after 3 failed attempts

## Quick Start

```bash
# 1. Set up Python venv and install dependencies
python -m venv .venv && .venv/Scripts/activate && pip install -r requirements.txt

# 2. Run lint and tests
make lint
make test

# 3. Start the webhook server (http://localhost:8000)
make dev

# 4. Or run everything in Docker
# (app + redis, hot-reloads on code changes)
docker compose up
```

## Makefile Targets
- `make dev`   – Start Flask webhook server (with reload)
- `make lint`  – Format code with black and isort
- `make test`  – Run all tests

## Day-1 Complete Checklist
- [x] GitHub App onboarding script
- [x] Health endpoint and smoke test
- [x] Docker Compose for app + Redis
- [x] Linting and formatting setup
- [x] Example .env and secure .gitignore

## Environment Variables

- `WEBHOOK_SECRET`: GitHub webhook secret
- `GH_APP_PK`: GitHub App private key (PEM, single line)
- `GH_APP_ID`: GitHub App ID
- `GH_CLIENT_ID`: GitHub App Client ID
- `REDIS_URL`: Redis connection string

## Development

- Run tests: `pytest -q`
- Start webhook: `make dev`

---

**TODOs:**  
- Add retry counter for failed PR attempts  
- Integrate Prometheus metrics for monitoring  