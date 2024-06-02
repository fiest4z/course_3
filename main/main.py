import func


def main():
    operations_list = func.import_operations()
    last_five_operations = func.five_last_operations(operations_list)
    sorted_operations = func.sorting_by_data(last_five_operations)
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
