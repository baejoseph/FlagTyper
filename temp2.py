import json
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)


# Load JSON data
with open(resource_path("data/flags.json"), "r", encoding="utf-8") as file:
    data = json.load(file)


names = []
for key, value in data.items():
    names.append(value["en"])

names.sort(key=len, reverse=True)

print(names[:10])