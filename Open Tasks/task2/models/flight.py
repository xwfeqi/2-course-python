class Flight:
    def __init__(self, flight_number, destination, departure_time, baggage_limit):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []
        self.baggage_limit = baggage_limit  # Загальний ліміт багажу (кг)

    def add_passenger(self, passenger, baggage_limit_per_person):
        """Додає пасажира до рейсу, перевіряючи ліміт багажу."""
        if passenger.baggage_weight > baggage_limit_per_person:
            raise ValueError(
                f"Багаж пасажира {passenger.name} перевищує ліміт {baggage_limit_per_person} кг."
            )

        total_baggage_weight = self.total_baggage_weight() + passenger.baggage_weight
        if total_baggage_weight > self.baggage_limit:
            raise ValueError(
                f"Додавання багажу призведе до перевищення загального ліміту багажу "
                f"{self.baggage_limit} кг на рейс."
            )

        self.passengers.append(passenger)

    def total_baggage_weight(self):
        """Обчислити загальну вагу багажу пасажирів на рейсі."""
        return sum(p.baggage_weight for p in self.passengers)
