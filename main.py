from db_operations import create_user, read_all, read_one, update_user, delete_user

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить пользователя")
        print("2. Показать всех пользователей")
        print("3. Найти пользователя по ID")
        print("4. Обновить имя пользователя")
        print("5. Удалить пользователя")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя: ")
            age = int(input("Введите возраст: "))
            create_user(name, age)

        elif choice == "2":
            users = read_all()
            for user in users:
                print(user)

        elif choice == "3":
            user_id = int(input("Введите ID пользователя: "))
            user = read_one(user_id)
            print(user if user else "Пользователь не найден")

        elif choice == "4":
            user_id = int(input("Введите ID пользователя: "))
            new_name = input("Введите новое имя: ")
            update_user(user_id, new_name)

        elif choice == "5":
            user_id = int(input("Введите ID пользователя: "))
            delete_user(user_id)

        elif choice == "0":
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
