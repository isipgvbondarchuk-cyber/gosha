import random
import math

def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))

    return question, correct_answer
