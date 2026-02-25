import prompt

def welcome_user():
    print("Добро пожаловать в VD-games!")
    name = prompt.string('Как вас зовут? ')
    print(f"Привет, {name}!")
    return name
