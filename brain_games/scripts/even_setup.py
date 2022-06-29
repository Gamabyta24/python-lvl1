"""File for setup game even."""
from brain_games.scripts.engine import run
from brain_games.games import brain_even
from brain_games.scripts import cli


def main():
    """MAIN_function for launch game even."""
    run(brain_even, cli)


if __name__ == "__main__":
    main()
