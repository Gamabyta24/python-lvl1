"""File for setup game gcd."""
from brain_games.scripts.engine import run
from brain_games.games import brain_gcd
from brain_games.scripts import cli


def main():
    """MAIN_function for launch game even."""
    run(brain_gcd, cli)


if __name__ == "__main__":
    main()
