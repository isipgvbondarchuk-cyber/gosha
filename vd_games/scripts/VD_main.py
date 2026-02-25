def show_message():
    print("Задание выполнено:")
    print("1. Создана структура проекта")
    print("2. Созданы все необходимые модули")
    print("3. Создана точка входа")

from vd_games.cli import welcome_user
from vd_games.scripts.VD_games import print_welcome

def main():
    welcome_user()
    print_welcome()
    print("Добро пожаловать в мир игр!")
    print("Приложение успешно запущено.")

if __name__ == "__main__":
    main()
