import json
from datetime import datetime


def read_json():
    """
    Функция считывает данные из json файла и возвращает их
    в качестве списка словарей
    :return: operations: считаный список словарей
    """

    with open("operations.json", "r") as file:
        operations_json = file.read()
        operations = json.loads(operations_json)

    return operations


def filter_data(array):
    """
    Каждый словарь обязательно должен содержать информацию о дате перевода,
    описание перевода, откуда и куда был сделан перевод, должна содержаться сумма
    перевода и валюта. Некоторые словари содержат недостаточно информации.
    Необходимо удалить такие словари из списка. Также нужно оставить только
    записи со статусом EXECUTED.
    :param array: список словарей
    :return: filtered_array: отфильтрованный список
    """

    required_data = ["date", "description", "from", "to", "operationAmount"]
    filtered_array = []

    for row in array:

        # Проверяем, что словарь не пустой
        if row:

            # Проверяем, что в словаре содержатся все необходимые данные
            if row["state"] == "EXECUTED" and all(x in row for x in required_data):
                filtered_array.append(row)

    return filtered_array

def sort_data(array):
    """
    Функция принимает на вход список словарей и сортирует их по дате
    :param array: список словарей
    :return: sorted_array: отсортированный список
    """

    sorted_array = sorted(array, key=lambda x: x['date'], reverse=True)
    return sorted_array
