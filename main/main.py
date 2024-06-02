import func


def main():
    list_operations = func.import_operations()
    five_operations = func.five_last_operations(list_operations)
    sorted_operations = func.sorting_by_data(five_operations)
    for operations in sorted_operations:
        if operations.get('from') is not None:
            hidden_number_from = func.hide_and_split(operations['from'])
            hidden_number_to = func.hide_and_split(operations['to'])
            print(f"{operations['date']} {operations['description']}\n"
                  f"{hidden_number_from} -> {hidden_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n")
        else:
            print(f"{operations['date']} {operations['description']}\n"
                  f"**** -> {hidden_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n")

main()

