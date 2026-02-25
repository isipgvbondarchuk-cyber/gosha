from vd_games.cli import welcome_user

def show_message():
    print("Задание выполнено:")
    print("1. Создана структура проекта")
    print("2. Созданы все необходимые модули")
    print("3. Создана точка входа")

def welcome_message():
    return "Начинаем новую игру!"

def print_welcome():
    message = welcome_message()
    print("=" * 50)
    print(message)
    print("=" * 50)

if __name__ == "__main__":
    welcome_user()
    print_welcome()
