import json
import os

FILE_PATH = "data/conversations.json"

def load_memory():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_memory(messages):
    with open(FILE_PATH, "w") as f:
        json.dump(messages, f, indent=2)