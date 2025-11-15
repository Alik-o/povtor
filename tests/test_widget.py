import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Счет 64686473678894779589", "Счет ** 9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет ** 4305"),
    ],
)
def test_mask_account_card_correct(card_number, expected):
    assert mask_account_card(card_number) == expected


def test_mask_account_card_incorrect():
    with pytest.raises(ValueError):
        mask_account_card("Счет 7365410843013j874305")
    with pytest.raises(ValueError):
        mask_account_card("MasterCard 71583007347267ll")
    with pytest.raises(ValueError):
        mask_account_card("Visa Classic 11")
    with pytest.raises(ValueError):
        mask_account_card("Счет")


def test_mask_no_account_card():
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize(
    "card_number, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-05-15T", "15.05.2024")]
)
def test_get_date_correct(card_number, expected):
    assert get_date(card_number) == expected


def test_get_date_incorrect():
    with pytest.raises(ValueError):
        get_date("2024-03-TT")


def test_get_date_no_date():
    with pytest.raises(ValueError):
        get_date("")
