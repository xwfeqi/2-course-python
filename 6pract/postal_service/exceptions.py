class InvalidParcelException(Exception):
    """Виняток для некоректних посилок."""
    pass

class ParcelNotFoundException(Exception):
    """Виняток для посилки, яку не знайдено."""
    pass
