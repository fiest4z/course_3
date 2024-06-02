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
    last_five = sorted(operations, key=lambda x: x['date'], reverse=True)[:5]
    return last_five


def formated_date(dt):
    return dt.strftime('%d.%m.%Y')


def update_operations(operations):
    new_operations = []
    for elem in operations:
        if elem and elem.get('date') is not None and elem.get('state') == "EXECUTED":
            elem['date'] = datetime.fromisoformat(elem['date'])
            new_operations.append(elem)
    return new_operations


def hide_and_split(bank):
    def hidden_account():
        account_number = '**' + numb[-4:]
        return account_number

    def hidden_card():
        card_number = numb[:6] + ('*' * 6) + numb[-4:]
        card_number = ' '.join(card_number[i * 4:(i + 1) * 4] for i in range(4))
        return card_number

    if bank is None:
        return 'Unknown'

    *name, numb = bank.split()
    if ' '.join(name) == "Счет":
        return f"Счет {hidden_account()}"
    else:
        return f"{' '.join(name)} {hidden_card()}"


def amount_and_currency(operation):
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    return f"{amount} {currency}"


def finish_info(operation):
    date = formated_date(operation.get('date'))
    desc = operation.get('description')
    source_from = hide_and_split(operation.get('from'))
    source_to = hide_and_split(operation.get('to'))
    amount_currency = amount_and_currency(operation)
    return f"{date} {desc}\n{source_from} -> {source_to}\n{amount_currency}\n"

