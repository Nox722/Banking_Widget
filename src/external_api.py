import os

import requests
from src.utils import get_data_from_json_file

def get_transaction_amount_in_rubles(transaction: dict) -> float:

    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
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
        return amount
    elif from_ in ("USD", "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
        headers = {"apikey": "2OkLJgmGvENWLtkRNIyBUHehi7yaqzTt"}

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}")

        result = response.json()["result"]
        return result
    else:
        raise ValueError(f"Unsupported currency: {from_}")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    file_path = os.path.join(root_dir, 'data', 'operations.json')

    data = get_data_from_json_file(file_path)
    some_dict = data[100]
    result_amount = get_transaction_amount_in_rubles(some_dict)
    print(result_amount)
