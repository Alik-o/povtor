import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = float(transaction["operationAmount"]["amount"])
        return amount
    else:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers, data=payload)
        return round(response.json()["result"], 2)
