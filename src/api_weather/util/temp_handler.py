import os, json

from setting import TEMP_DIR_PATH


def get_temp_path(filename="temp.json"):
    return os.path.join(TEMP_DIR_PATH, filename)


def save_to_temp(data, filename="temp.json"):
    os.makedirs(TEMP_DIR_PATH, exist_ok=True)
    with open(get_temp_path(filename), 'w') as f:
        json.dump(data, f)


def get_from_temp(filename="temp.json"):
    data = {}
    with open(get_temp_path(filename), 'r') as f:
        data = json.load(f)
    return data
