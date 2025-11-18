from unittest.mock import patch

from src.external_api import get_amount_rub

transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


@patch("requests.request")
def test_get_amount_usd(mock_request):
    mock_request.return_value.json.return_value = {"result": 100}
    assert get_amount_rub(transaction_usd) == 100
    mock_request.assert_called_once()


def test_get_amount_rub():
    assert get_amount_rub(transaction_rub) == 31957.58
