import os
from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests
from dotenv import load_dotenv

from src import get_transaction_amount_in_rubles

load_dotenv()
api_key = os.getenv("API_KEY")


def test_get_transaction_amount_in_rubles(transaction_rub: dict[str, Any]) -> None:
    """передаем транзакцию изначально в рублях"""
    result = get_transaction_amount_in_rubles(transaction_rub)
    assert result == 67314.7


def test_get_transaction_amount_in_rubles_wrong_currency(transaction_jpy: dict[str, Any]) -> None:
    """передаем транзакцию с неподдерживаемой валютой"""
    with pytest.raises(ValueError) as e:
        get_transaction_amount_in_rubles(transaction_jpy)
    assert e.value.args[0] == "Currency not recognized. Supported: USD, EUR, RUB."


def test_get_transaction_amount_in_rubles_empty_dict() -> None:
    """передаем пустой словарь"""
    with pytest.raises(KeyError) as e:
        get_transaction_amount_in_rubles({})
    assert e.value.args[0] == "Required keys in transaction are missing."


def test_get_transaction_amount_in_rubles_wrong_type() -> None:
    """передаем другой тип данных (не словарь)"""
    with pytest.raises(TypeError) as e:
        get_transaction_amount_in_rubles([])  # type: ignore
    assert e.value.args[0] == "Transaction must be a dictionary."


@patch("requests.get")
def test_get_transaction_amount_in_rubles_api(mock_get: Mock, transaction_usd: dict[str, Any]) -> None:
    """проверка правильности обработки успешного ответа API"""
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 794303.812498}

    result = get_transaction_amount_in_rubles(transaction_usd)
    assert result == 794303.812498
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=9824.07",
        headers={"apikey": api_key},
    )


@patch("requests.get")
def test_get_transaction_amount_in_rubles_error(mock_get: Mock, transaction_usd: dict[str, Any]) -> None:
    """проверка обработки исключения HTTPError при неудачном HTTP-запросе"""
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Request failed with status code 404")
    with pytest.raises(requests.exceptions.HTTPError) as e:
        get_transaction_amount_in_rubles(transaction_usd)
    assert str(e.value) == "Request failed with status code 404"
