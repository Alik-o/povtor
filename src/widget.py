from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Маскирует номер счета или карты"""
    if card_number and len(card_number) > 20:
        if card_number[0:4] == "Счет":
            account_namber = card_number[5:]
            if account_namber.isdigit() and len(account_namber) == 20:
                mask = get_mask_account(card_number[5:])
                return f"{card_number[0:4]} {mask}"
            else:
                raise ValueError("Неверный номер счета")
        else:
            card_number_mask = card_number[-16:]
            if card_number_mask.isdigit() and len(card_number_mask) == 16:
                mask = get_mask_card_number(card_number_mask)
                return f"{card_number[:-16]}{mask}"
            else:
                raise ValueError("Неверный номер карты")
    else:
        raise ValueError("Отсутствует номер счета или карты")


def get_date(date: str) -> str:
    """Преобразует дату в формат dd.mm.yyyy"""
    if date:
        day = date[8:10]
        month = date[5:7]
        year = date[0:4]
        if day.isdigit() and month.isdigit() and year.isdigit():
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
        else:
            raise ValueError("Некорректная дата")
    else:
        raise ValueError("Отсутствует дата")
