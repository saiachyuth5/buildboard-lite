import os
import redis
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(REDIS_URL)

def enqueue_task(payload):
    r.lpush("buildboard:tasks", json.dumps(payload))

def dequeue_task():
    task = r.rpop("buildboard:tasks")
    if task:
        return json.loads(task)
    return None

# TODO: Add retry counter logic for failed tasks (Day-2) 