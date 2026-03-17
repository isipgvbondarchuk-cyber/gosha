import prompt

ROUNDS_COUNT = 3

def run_game(game_module, description):
    name = prompt.string('Как тебя зовут? ')
    print(f"Привет, {name}!")
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Вопрос: {question}")
        answer = input("Твой ответ: ").strip()

        if answer == correct_answer:
            print("Правильно!")
        else:
            print(f"'{answer}' — неправильный ответ ;( Правильный ответ: '{correct_answer}'.")
            print(f"Попробуй ещё раз, {name}!")
            return

    print(f"Поздравляю, {name}!")
