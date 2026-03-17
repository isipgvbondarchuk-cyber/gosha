from vd_games.games import progression
from vd_games.games.engine import run_game


def main():
    description = "Какого числа не хватает в прогрессии?"
    run_game(progression, description)


if __name__ == "__main__":
    main()
