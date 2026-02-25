import random
from vd_games.cli import welcome_user

def is_even(number):
    return number % 2 == 0

def play_game():
    name = welcome_user()
    print('Отвечай "да", если число чётное, иначе "нет".')

    correct_answers = 0
    needed_correct = 3

    while correct_answers < needed_correct:
        number = random.randint(1, 100)
        print(f"Вопрос: {number}")

        answer = input("Твой ответ: ").strip().lower()

        if answer == "да" or answer == "yes" or answer == "y":
            user_choice = "да"
            is_even_answer = True
        elif answer == "нет" or answer == "no" or answer == "n":
            user_choice = "нет"
            is_even_answer = False
        else:
            print(f"'{answer}' - неправильный ответ. Нужно 'да' или 'нет'.")
            print(f"Попробуй снова, {name}!")
            return

        correct_answer_bool = is_even(number)
        correct_answer_text = "да" if correct_answer_bool else "нет"

        if is_even_answer == correct_answer_bool:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"'{user_choice}' - неправильный ответ ;( Правильный ответ был '{correct_answer_text}'.")
            print(f"Попробуй снова, {name}!")
            return

    print(f"Поздравляю, {name}!")

def main():
    play_game()

if __name__ == "__main__":
    main()
