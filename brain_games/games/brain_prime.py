"""PRIME GAME."""

import random


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
    """Game func.

    Returns:
        string with 1 number.
        right answer.
    """
    num_for_operation = 0
    number = random_number()
    for _ in range(2, number // 2 + 1):
        if number % _ == 0:
            num_for_operation = num_for_operation + 1
    if num_for_operation <= 0:
        return number, "yes"
    return number, "no"
