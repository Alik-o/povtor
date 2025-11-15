def get_mask_card_number(card_number: str) -> str:
    """Создает маску карты"""
    mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask


def get_mask_account(account_number: str) -> str:
    """Создает маску счета"""
    mask = f"** {account_number[-4:]}"
    return mask
