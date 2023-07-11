import pytest
from utils import operations


def test_read_json():
    with pytest.raises(FileNotFoundError):
        operations.read_json()


def test_filter_data():
    # Словарь, удовлетворяющий всем условиям
    dictionary1 = {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"}

    # Словарь, содержащий недостаточно информации
    dictionary2 = {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199"}

    # Словарь с невыполненной операцией
    dictionary3 = {"id": 441945886, "state": "CANCELED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"}

    assert operations.filter_data([{}]) == []
    assert operations.filter_data([dictionary1]) == [dictionary1]
    assert operations.filter_data([dictionary2]) == []
    assert operations.filter_data([dictionary3]) == []


def test_sort_data():
    array1 = [{"date": "2019-04-04T23:20:05.206878"}, {"date": "2019-08-26T10:50:58.294041"},
              {"date": "2018-06-30T02:08:58.425572"}]

    array2 = [{"date": "2019-04-04T23:20:05.206878"}, {"date": "2019-04-26T10:50:58.294041"},
              {"date": "2019-04-30T02:08:58.425572"}]

    assert operations.sort_data(array1) == [{"date": "2019-08-26T10:50:58.294041"},
                                            {"date": "2019-04-04T23:20:05.206878"},
                                            {"date": "2018-06-30T02:08:58.425572"}]

    assert operations.sort_data(array2) == [{"date": "2019-04-30T02:08:58.425572"},
                                            {"date": "2019-04-26T10:50:58.294041"},
                                            {"date": "2019-04-04T23:20:05.206878"}]


def test_right_format():
    dictionary1 = {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"}

    dictionary2 = {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                   "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                   "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                   "to": "Счет 75651667383060284188"}

    string1 = """26.8.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"""

    string2 = """4.4.2019 Перевод со счета на счет\nСчет 1970 86** **** **** 8542 -> Счет **4188\n79114.93 USD\n"""

    assert operations.right_format(dictionary1) == string1
    assert operations.right_format(dictionary2) == string2
