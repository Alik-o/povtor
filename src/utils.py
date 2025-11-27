import json
import logging
import os

import pandas as pd

from config import DATA_DIR, LOG_DIR

path_log = os.path.join(LOG_DIR, "utils.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=str(path_log),
    encoding="utf-8",
    filemode="w",
)
utils_logger = logging.getLogger(__name__)

path = os.path.join(DATA_DIR, "operations.json")


def create_dir(dir_path: str = path):
    """Возвращает список словарей из json файла"""
    try:
        if dir_path.endswith(".json"):
            utils_logger.debug(f"Пытаемся прочитать json файл {dir_path}")
            with open(dir_path, "r", encoding="utf-8") as f:
                operations = json.load(f)
            utils_logger.debug(f"Успешно прочитан файл {dir_path}")
        elif dir_path.endswith(".xlsx"):
            utils_logger.debug(f"Пытаемся прочитать xlsx файл {dir_path}")
            operations = pd.read_excel(dir_path)
            utils_logger.debug(f"Успешно прочитан файл {dir_path}")
        elif dir_path.endswith(".csv"):
            utils_logger.debug(f"Пытаемся прочитать csv файл {dir_path}")
            operations = pd.read_csv(dir_path)
            utils_logger.debug(f"Успешно прочитан файл {dir_path}")
        return operations
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении файла: {e}")
        return []
