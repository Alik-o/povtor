from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Маскирует номер счета или карты"""
    if card_number[0:4] == "Счет":
        mask = get_mask_account(card_number[5:])
        return f"{card_number[0:5]} {mask}"
    else:
        mask = get_mask_card_number(card_number[-16:])
        return f"{card_number[:-16]} {mask}"


def get_date(date: str) -> str:
    """Преобразует дату в формат dd.mm.yyyy"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    card_number = "Счет 73654108430135874305"
    print(mask_account_card(card_number))
    card_number = "MasterCard 7158300734726758"
    print(mask_account_card(card_number))
    date = "2024-03-11T02:26:18.671407"
    print(get_date(date))
