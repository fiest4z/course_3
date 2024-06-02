from datetime import datetime
import json


def import_operations():
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def convert_time():
    pass


def five_last_operations():
    pass
