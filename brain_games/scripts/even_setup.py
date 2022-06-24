from brain_games.scripts.engine import run, welcome_user
from brain_games.games import brain_even


def main():
    run(brain_even, welcome_user)


if __name__ == "__main__":
    main()
