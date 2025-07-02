import os
from flask import Flask, request, jsonify
from app.bot_logic import handle_issue_labeled
from app.queue import enqueue_task

app = Flask(__name__)

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.headers.get("X-GitHub-Event")
    payload = request.json

    if event == "issues" and payload.get("action") == "labeled":
        label = payload["label"]["name"]
        if label == "ai-fix":
            enqueue_task(payload)
            return jsonify({"status": "queued"}), 202
    return jsonify({"status": "ignored"}), 200

@app.route("/ping")
def ping():
    return "pong", 200

# TODO: Add Prometheus metrics endpoint here (Day-2) 