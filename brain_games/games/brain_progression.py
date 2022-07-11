"""Progression game GAME."""

import random


def make_quest():
    """Make quest for user.

    Returns:
        String when says what user own do.
    """
    return "What number is missing in the progression?"


def try_count():
    """Tryes in even game.

    Returns:
        Number of tryes.
    """
    return 3


def random_number():
    """Randomizer.

    Returns:
        random number between 1 and 100.
    """
    return random.randint(1, 100)


def game_stats():
    """Game func.

    Returns:
        mass with 1 unknown number.
        right answer.
    """
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    empty_space = random.randint(0, 9)
    mass = []
    for _ in range(10):
        number_for_operation = start + step
        if _ == empty_space:
            mass.append("..")
            right_answer = number_for_operation
            start = number_for_operation
            continue
        mass.append(number_for_operation)
        start = number_for_operation
    return mass, f"{right_answer}"
