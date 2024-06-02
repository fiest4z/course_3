from datetime import datetime
import json


def import_operations():
    """
    Импорт операций из operations.json
    """
    with open('../operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def five_last_operations(operations):
    """
    Последние 5 операций
    """
    sorted_operations = sorted(operations, key=lambda x: x.get('date', '0'))
    last_five = sorted_operations[:6]
    return last_five

def sorting_by_data(last_five):
    del last_five[0]
    for x in last_five:
        x['date'] = datetime.fromisoformat(x['date']).strftime('%d.%m.%y')
    return last_five


print(five_last_operations(import_operations()))