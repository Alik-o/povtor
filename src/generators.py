from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[list[dict]]:
    """Фильтрует транзакции по валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Возвращает описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(initial_value: int, final_value: int) -> Iterator[str]:
    """Генерирует последовательность номеров карт"""
    for i in range(initial_value, final_value + 1):
        len_number = 16 - len(str(i))
        card_number = "0" * len_number + str(i)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[-4:]}"
