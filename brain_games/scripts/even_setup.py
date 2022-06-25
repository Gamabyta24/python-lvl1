from pydoc import cli
from brain_games.scripts.engine import run
from brain_games.games import brain_even
from brain_games.scripts import cli

def main():
    run(brain_even,cli)


if __name__ == "__main__":
    main()
