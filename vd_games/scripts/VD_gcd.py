from vd_games.games import gcd
from vd_games.games.engine import run_game

def main():
    description = "Найди наибольший общий делитель этих чисел."
    run_game(gcd, description)

if __name__ == "__main__":
    main()
