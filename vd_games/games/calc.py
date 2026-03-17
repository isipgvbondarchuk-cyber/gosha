import random
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def get_question_and_answer():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(list(OPERATIONS.keys()))

    question = f"{a} {op} {b}"
    correct_answer = str(OPERATIONS[op](a, b))

    return question, correct_answer
