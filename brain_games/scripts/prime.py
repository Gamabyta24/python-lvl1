"""File for setup game prime."""
from brain_games.scripts.engine import run
from brain_games.games import brain_prime
from brain_games.scripts import cli


def main():
    """MAIN_function for launch game even."""
    run(brain_prime, cli)


if __name__ == "__main__":
    main()
