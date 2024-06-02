import pytest
from main.func import (five_last_operations,
                       formated_date,
                       hide_and_split,
                       amount_and_currency,
                       import_operations,
                       update_operations)


from datetime import datetime
import os

def test_import_operations():
    with pytest.raises(FileNotFoundError):
        import_operations()


def test_five_last_operations():
    assert five_last_operations([]) == []
    assert five_last_operations([
        {'date': -1},
        {'date': 1},
        {'date': 0},
        {'date': 15},
        {'date': 10},
        {'date': 5}
    ]) == [{'date': 15}, {'date': 10}, {'date': 5}, {'date': 1}, {'date': 0}]

def test_hide_and_split():
    assert hide_and_split("Счет 64686473678894779589") == "Счет **9589"
    assert hide_and_split("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert hide_and_split(None) == "Unknown"

def test_formated_date():
    with pytest.raises(AttributeError):
        formated_date('data')
    assert formated_date(datetime.fromisoformat("2018-03-23T10:45:06.972075")) == '23.03.2018'

def test_amount_and_currency():
    assert amount_and_currency({
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"}) == '9824.07 USD'

@pytest.mark.parametrize('list_dict, expected', [
    ([{}], []),
    ([{"date": "2019-07-12T20:41:47.882230", "state": "EXECUTED"}],
     [{"date": datetime.fromisoformat("2019-07-12T20:41:47.882230"), "state": "EXECUTED"}]),
    ([{"date": "2019-07-12T20:41:47.882230"}], []),
    ([{"state": "EXECUTED"}], []),
])
def test_update_operations(list_dict, expected):
    assert update_operations(list_dict) == expected
