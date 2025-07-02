# BuildBoard-Lite

**BuildBoard-Lite** is an open-source GitHub App bot that:
- Listens for `issues.labeled:ai-fix`
- Checks out the repo in a Docker sandbox
- Asks an LLM to patch ≤10 files / ≤400 LOC
- Opens/updates a PR until CI is green
- Escalates with label `needs-human` after 3 failed attempts

## Quickstart

1. **Clone & configure:**
   ```bash
   git clone https://github.com/youruser/buildboard-lite.git
   cd buildboard-lite
   cp .env.example .env
   ```

2. **Create a GitHub App:**  
   Run the onboarding script:
   ```bash
   python scripts/init_app.py
   ```
   Follow the prompts and update `.env` with your App credentials.

3. **Run locally:**
   ```bash
   docker compose up
   ```

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