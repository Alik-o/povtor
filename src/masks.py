import logging
import os

from config import LOG_DIR

path = os.path.join(LOG_DIR, "masks.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=str(path),
    encoding="utf-8",
    filemode="w",
)
masks_logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Создает маску карты"""
    masks_logger.debug(f"Получаем номе карты {card_number}")
    mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masks_logger.debug(f"Создаем маску карты {mask}")
    return mask


def get_mask_account(account_number: str) -> str:
    """Создает маску счета"""
    masks_logger.debug(f"Получаем номер счета {account_number}")
    mask = f"** {account_number[-4:]}"
    masks_logger.debug(f"Создаем маску счета {mask}")
    return mask
