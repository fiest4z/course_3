import func


def main():
    operations = func.import_operations()
    new_operations = func.update_operations(operations)
    last_five = func.five_last_operations(new_operations)
    for elem in last_five:
        print(func.finish_info(elem))


main()
