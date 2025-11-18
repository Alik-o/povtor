import json
import os

from config import DATA_DIR

path = os.path.join(DATA_DIR, "operations.json")


def create_dir(dir_path: str = path):
    """Возвращает список словарей из json файла"""
    try:
        with open(dir_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
        return operations
    except Exception:
        return []
