from vd_games.games import prime
from vd_games.games.engine import run_game

def main():
    description = 'Отвечай "да", если число простое, иначе "нет".'
    run_game(prime, description)

if __name__ == "__main__":
    main()
