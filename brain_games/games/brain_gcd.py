"""GCD GAME."""

import random


def make_quest():
    return "Find the greatest common divisor of given numbers."


def try_count():
    """Tryes in even game.

    Returns:
        Number of tryes.
    """
    return 3


def random_number():
    """Randomizer.

    Returns:
        random number between 1 and 25.
    """
    return random.randint(1, 100)


def game_stats():
    number1 = random_number()
    number2 = random_number()
    copy1 = number1
    copy2 = number2
    while copy1 != 0 and copy2 != 0:
        if copy1 > copy2:
            copy1 = copy1 % copy2
        elif copy2 > copy1:
            copy2 = copy2 % copy1
    num_nod = copy1 + copy2
    return f"{number1},{number2}", f"{num_nod}"
