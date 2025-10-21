import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if not isinstance(transaction, dict):
        raise TypeError("Transaction must be a dictionary.")

    try:
        code = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
    except KeyError:
        raise KeyError("Required keys in transaction are missing.")

    to = "RUB"

    currency_map = {
        "USD": "USD",
        "EUR": "EUR",
        "RUB": "RUB",
    }

    from_ = currency_map.get(code)

    if from_ is None:
        raise ValueError("Currency not recognized. Supported: USD, EUR, RUB.")

    if from_ == "RUB":
        return float(amount)
    elif from_ in ("USD", "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()["result"]
        return float(result)
    else:
        raise ValueError(f"Unsupported currency: {from_}")
