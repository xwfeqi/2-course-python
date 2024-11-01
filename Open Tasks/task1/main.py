import json

def get_unique_values_from_json(file_path, key):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            unique_values = {item[key] for item in data if key in item}
            return list(unique_values)
        else:
            raise ValueError("JSON data is not a list of dictionaries.")
    
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except json.JSONDecodeError:
        print("Файл містить некоректні дані у форматі JSON.")
    except ValueError as e:
        print(f"Помилка: {e}")

    return []
result = get_unique_values_from_json("data.json", "name")
print(result)
