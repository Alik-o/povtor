def get_mask_card_number(card_number: str) -> str:
    """Создает маску карты"""
    mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask


def get_mask_account(account_number: str) -> str:
    """Создает маску счета"""
    mask = f"** {account_number[-4:]}"
    return mask


if __name__ == "__main__":
    card_number = "1111222233334444"
    print(get_mask_card_number(card_number))
    account_number = "1234567890123456"
    print(get_mask_account(account_number))
