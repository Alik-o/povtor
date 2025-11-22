import json
import logging
import os

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
        utils_logger.debug(f"Пытаемся прочитать файл {dir_path}")
        with open(dir_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
        utils_logger.debug(f"Успешно прочитан файл {dir_path}")
        return operations
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении файла: {e}")
        return []
