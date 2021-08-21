
import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
KEYS_PATH = os.path.join(BASE_DIR,"KEYS.json")

def get_KEY(keyname):

    if os.path.exists(KEYS_PATH):
        with open(KEYS_PATH) as raw_json:
            data = json.load(raw_json)
            return data[keyname]
    else:
        return os.environ[keyname]

def is_DEBUG():
    if os.path.exists(KEYS_PATH):
        with open(KEYS_PATH) as raw_json:
            data = json.load(raw_json)

            if data['DEBUG'] == "TRUE":
                return True
            else:
                return False

    else:
            if os.environ['DEBUG'] == "TRUE":
                return True
            else:
                return False