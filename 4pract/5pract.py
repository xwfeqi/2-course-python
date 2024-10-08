class ChatRoom:
    def __init__(self):
        self.messages = []  # Список для збереження всіх повідомлень
        self.users = {}     # Список зареєстрованих користувачів

    def register_user(self, user):
        self.users[user.name] = user

    def send_message(self, from_user, message, to_user=None):
        self.messages.append((from_user, message, to_user))
        if to_user:
            recipient = self.users.get(to_user)
            if recipient:
                recipient.receive_message(f"Private message to {to_user} from {from_user}: {message}")
            else:
                print(f"User {to_user} not found.")

    def show_messages(self):
        if not self.messages:
            print("No messages yet.")
        for i, (from_user, message, to_user) in enumerate(self.messages):
            if to_user:
                print(f"{i}: Private to {to_user} from {from_user}: {message}")
            else:
                print(f"{i}: {from_user} (public): {message}")

    def get_message(self, index):
        if 0 <= index < len(self.messages):
            return self.messages[index]
        else:
            return None


class User:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room
        chat_room.register_user(self)  # Реєструємо користувача в ChatRoom

    def send_message(self, message, to_user=None):
        # Відправляємо повідомлення через ChatRoom
        self.chat_room.send_message(self.name, message, to_user)

    def receive_message(self, message):
        print(f"{self.name} отримав повідомлення: {message}")

    def reply_to_message(self, index, reply_message):
        # Отримуємо повідомлення через ChatRoom
        original_message = self.chat_room.get_message(index)
        if original_message:
            from_user, message, to_user = original_message
            # Якщо повідомлення публічне або приватне для користувача
            if not to_user or to_user == self.name:
                self.chat_room.send_message(self.name, reply_message, to_user=from_user)
            else:
                print("You cannot reply to this message.")
        else:
            print("Invalid message index.")


# Приклад використання:
chat_room = ChatRoom()

# Створюємо двох користувачів
user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)

# Цикл для переписки
while True:
    print("\nДії:")
    print("1. Alice: Надіслати приватне повідомлення Bob")
    print("2. Bob: Надіслати приватне повідомлення Alice")
    print("3. Відповісти на повідомлення")
    print("4. Переглянути всі повідомлення")
    print("5. Вийти з програми")

    choice = input("Виберіть дію (1-5): ")

    if choice == '1':
        message = input("Alice вводить приватне повідомлення Bob: ")
        user1.send_message(message, to_user="Bob")

    elif choice == '2':
        message = input("Bob вводить приватне повідомлення Alice: ")
        user2.send_message(message, to_user="Alice")

    elif choice == '3':
        chat_room.show_messages()
        index = int(input("Введіть індекс повідомлення для відповіді: "))
        user = input("Виберіть користувача (Alice/Bob): ")
        if user == "Alice":
            reply_message = input("Alice вводить відповідь: ")
            user1.reply_to_message(index, reply_message)
        elif user == "Bob":
            reply_message = input("Bob вводить відповідь: ")
            user2.reply_to_message(index, reply_message)
        else:
            print("Невірний вибір користувача.")

    elif choice == '4':
        chat_room.show_messages()

    elif choice == '5':
        print("Вихід з програми...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")
