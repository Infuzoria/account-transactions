import json


def read_json():
    """
    Функция считывает данные из json файла и возвращает их
    в качестве списка словарей
    """

    with open("operations.json", "r") as file:
        operations_json = file.read()
        operations = json.loads(operations_json)

    return operations
