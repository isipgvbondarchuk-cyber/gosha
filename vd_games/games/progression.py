import random


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    return ' '.join(progression), correct_answer


def get_question_and_answer():
    question, correct_answer = generate_progression()
    return question, correct_answer
