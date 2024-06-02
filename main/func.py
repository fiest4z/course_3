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
        x['date'] = datetime.fromisoformat(x['date']).strftime('%d.%m.%Y')
    return last_five

def hide_and_split(card):
    card_number = card.split()[-1]
    if len(card_number) == 16:
        hidden_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        parts, part_size = len(hidden_number), len(hidden_number) // 4
        closed_number = f"{card[:-len(card_number)]} {' '.join([hidden_number[i:i + part_size] for i in range(0, parts, part_size)])}"
    else:
        hidden_number = f"{card[:len(card_number)]}{('**' + (card_number[-4:]))}"
    return hidden_number




