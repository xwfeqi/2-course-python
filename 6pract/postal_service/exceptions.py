class InvalidParcelException(Exception):
    print("Виняток для некоректних посилок.")
    pass

class ParcelNotFoundException(Exception):
    print("Виняток для посилки, яку не знайдено.")
    pass
