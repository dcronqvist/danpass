import json
import os

fi = os.getcwd() + "/config.json"

def load_settings():
    with open(fi, "rb") as f:
        s = json.load(f)
        return s
    return None

def save_settings(settings):
    with open(fi, "w") as f:
        json.dump(settings, f, indent=4)

def get_setting(key, default=None):
    settings = load_settings()
    if key in settings:
        return settings.get(key, default)
    return default

def set_setting(key, value):
    settings = load_settings()
    print(settings)
    settings[key] = value
    save_settings(settings)
    
    