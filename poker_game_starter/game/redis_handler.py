import json
import redis

r = redis.Redis(host='redis', port=6379, db=0)

def save_room(room_code, data):
    r.set(room_code, json.dumps(data))

def load_room(room_code):
    val = r.get(room_code)
    return json.loads(val) if val else None

def delete_room(room_code):
    r.delete(room_code)
