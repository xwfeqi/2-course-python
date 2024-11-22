class AirportSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        """Додати рейс, перевіряючи конфлікти часу та місця."""
        for existing_flight in self.flights:
            if (
                existing_flight.destination == flight.destination
                and existing_flight.departure_time == flight.departure_time
            ):
                raise ValueError(
                    f"Рейс у {flight.destination} на {flight.departure_time} вже існує."
                )
        self.flights.append(flight)

    def show_flights(self):
        """Вивести інформацію про всі рейси."""
        if not self.flights:
            print("Немає запланованих рейсів.")
        for flight in self.flights:
            print(
                f"Рейс {flight.flight_number}: {flight.destination} о {flight.departure_time}."
            )
            print(
                f"  Пасажири: {len(flight.passengers)}, "
                f"Загальна вага багажу: {flight.total_baggage_weight()} кг, "
                f"Ліміт: {flight.baggage_limit} кг."
            )
            if flight.passengers:
                print("  Список пасажирів:")
                for passenger in flight.passengers:
                    print(f"    - {passenger.name}, багаж: {passenger.baggage_weight} кг")
