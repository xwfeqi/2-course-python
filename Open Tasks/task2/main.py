from models.flight import Flight
from models.passenger import Passenger
from services.airport import AirportSystem


def initialize_flights(airport_system):
    """Додати початкові рейси до системи."""
    initial_flights = [
        Flight("PS101", "Київ-Львів", "10:00", 100),
        Flight("PS102", "Київ-Одеса", "12:00", 120),
        Flight("PS103", "Київ-Львів", "10:00", 100),  # Колізія рейсу
        Flight("PS103", "Київ-Харків", "14:00", 150),
    ]

    for flight in initial_flights:
        try:
            airport_system.add_flight(flight)
        except ValueError as e:
            print(f"Помилка: {e}")


def main():
    # Ініціалізація системи
    airport_system = AirportSystem()
    initialize_flights(airport_system)

    while True:
        print("\n--- Меню ---")
        print("1. Додати пасажира до рейсу")
        print("2. Показати всі рейси")
        print("3. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            print("\n--- Список рейсів ---")
            for flight in airport_system.flights:
                print(
                    f"{flight.flight_number}: {flight.destination} о {flight.departure_time} "
                    f"(Ліміт багажу: {flight.baggage_limit} кг, "
                    f"Використано: {flight.total_baggage_weight()} кг)"
                )

            flight_number = input("\nВведіть номер рейсу: ")
            flight = next(
                (f for f in airport_system.flights if f.flight_number == flight_number),
                None,
            )

            if not flight:
                print(f"Рейс {flight_number} не знайдено.")
                continue

            name = input("Ім'я пасажира: ")
            try:
                baggage_weight = float(input("Вага багажу (кг): "))
                passenger = Passenger(name, baggage_weight)
                baggage_limit_per_person = 25  # Ліміт на пасажира
                flight.add_passenger(passenger, baggage_limit_per_person)
                print(f"Пасажира {name} додано до рейсу {flight_number}.")
            except ValueError as e:
                print(f"Помилка: {e}")

        elif choice == "2":
            airport_system.show_flights()

        elif choice == "3":
            print("Вихід із системи...")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
