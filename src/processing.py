def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Фильтрует транзакции по статусу"""
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(transactions: list, ascending: bool = True) -> list:
    """Сортирует транзакции по дате"""
    return sorted(transactions, key=lambda transaction: transaction["date"], reverse=ascending)
