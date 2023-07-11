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


def right_format(dictionary):

    """
    Функция принимает на вход словарь и выводит необходимые данные 
    в слудующем формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    
    :param dictionary: словарь из списка
    :return: text: данные в верном формате
    """

    # Считываем дату и записываем её в формате дд.мм.гггг
    dt_string = dictionary["date"]
    dt_object = datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%S.%f")
    data = f"{dt_object.day}.{dt_object.month}.{dt_object.year}"

    # Формируем маску для счета отправителя
    account_from = dictionary["from"]
    account_from = account_from.split()
    final_row = ' '.join(account_from[:-1])

    account_from = f"{account_from[-1][:6]}{(len(account_from[-1]) - 10)*'*'}{account_from[-1][-4:]}"
    for i in range(0, len(account_from), 4):
        final_row += " "
        final_row += account_from[i: i+4]

    # Формируем маску для счета получателя
    account_to = dictionary["to"]
    account_to = account_to.split()
    account_string_to = f"{' '.join(account_to[:-1])} **{account_to[-1][-4:]}"

    #Формируем текст, который будет выведен на экран
    text = f'{data} {dictionary["description"]}\n{final_row} -> ' \
           f'{account_string_to}\n{dictionary["operationAmount"]["amount"]} ' \
           f'{dictionary["operationAmount"]["currency"]["name"]}\n'

    return text
