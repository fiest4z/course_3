import pytest
from main import func
from datetime import datetime


def test_five_last_operations():
    assert func.five_last_operations([]) == []
    assert func.five_last_operations([
        {'date': -1},
        {'date': 1},
        {'date': 0},
        {'date': 15},
        {'date': 10},
        {'date': 5}
    ]) == [{'date': 15}, {'date': 10}, {'date': 5}, {'date': 1}, {'date': 0}]

