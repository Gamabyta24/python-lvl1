"""GCD GAME."""

import random
from math import gcd


def make_quest():
    """Make quest for user.

    Returns:
        Number string with quest.
    """
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
    """Stats for user.

    Returns:
        two numbers and right answer.
    """
    number1 = random_number()
    number2 = random_number()
    num_nod = gcd(number1, number2)
    return f"{number1},{number2}", f"{num_nod}"
