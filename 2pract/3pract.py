import os

def caesar_cipher(text, shift, decrypt=False):
    result = []
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        encrypted_content = caesar_cipher(content, shift)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(encrypted_content)

        print(f"Файл успішно зашифровано та збережено як '{output_file}'.")

    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")
    except IOError as e:
        print(f"Помилка введення/виведення: {e}")

def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        decrypted_content = caesar_cipher(content, shift, decrypt=True)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(decrypted_content)

        print(f"Файл успішно розшифровано та збережено як '{output_file}'.")

    except FileNotFoundError:
        print(f"Помилка: файл '{input_file}' не знайдено.")
    except IOError as e:
        print(f"Помилка введення/виведення: {e}")

# Основна функція
def main():
    try:
        input_file = input("Введіть ім'я файлу для шифрування/розшифрування: ")
        
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Файл '{input_file}' не знайдено.")
        
        mode = input("Оберіть режим (encrypt/decrypt): ").strip().lower()
        shift = int(input("Введіть зсув для шифру Цезаря: "))

        output_file = input("Введіть ім'я файлу для збереження результату: ")

        if mode == 'encrypt':
            encrypt_file(input_file, output_file, shift)
        elif mode == 'decrypt':
            decrypt_file(input_file, output_file, shift)
        else:
            print("Невідомий режим. Використовуйте 'encrypt' для шифрування або 'decrypt' для розшифрування.")
    
    except ValueError:
        print("Помилка: зсув повинен бути цілим числом.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

if __name__ == "__main__":
    main()
