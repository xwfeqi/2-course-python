import time
from datetime import datetime, timedelta
import heapq

# Список запланованих завдань (з пріоритетом на основі часу виконання)
tasks = []

# Планувальник (черга пріоритетів)
def schedule_task(time_to_run, func, is_repeating=False, interval=None):
    heapq.heappush(tasks, (time_to_run, func, is_repeating, interval))

# Декоратор для запланованих завдань
def schedule(run_time):
    def decorator(func):
        if isinstance(run_time, int):  # Якщо інтервал у секундах
            next_run = datetime.now() + timedelta(seconds=run_time)
            schedule_task(next_run, func, is_repeating=True, interval=run_time)
        else:  # Якщо конкретний час (формат HH:MM:SS)
            today = datetime.now().replace(microsecond=0)
            target_time = datetime.strptime(run_time, '%H:%M:%S').replace(
                year=today.year, month=today.month, day=today.day)
            if target_time < today:
                target_time += timedelta(days=1)  # Якщо час вже минув, переносимо на наступний день
            schedule_task(target_time, func, is_repeating=False)
        return func
    return decorator

# Генератор циклу подій (event loop)
def event_loop():
    while True:
        if tasks:
            now = datetime.now()
            next_time, func, is_repeating, interval = heapq.heappop(tasks)
            if next_time <= now:
                func()  # Виконуємо завдання
                if is_repeating:
                    next_time = now + timedelta(seconds=interval)
                    schedule_task(next_time, func, is_repeating=True, interval=interval)
            else:
                heapq.heappush(tasks, (next_time, func, is_repeating, interval))  # Повертаємо завдання назад
        yield  # Пауза між перевірками

# Приклад використання декоратора
@schedule('15:30:00')
def task_once():
    print(f"Одноразове завдання виконано о {datetime.now()}")

@schedule(10)  # Запуск кожні 10 секунд
def repeating_task():
    print(f"Повторюване завдання виконано о {datetime.now()}")

# Старт циклу подій
event_gen = event_loop()

# Основний цикл програми
while True:
    next(event_gen)
    time.sleep(1)  # Чекати 1 секунду між кожною ітерацією
