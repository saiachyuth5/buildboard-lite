import pytest
from app.github_webhook import app

def test_ping():
    client = app.test_client()
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.data == b"pong" 