"""File with game quest."""
import random


def make_quest():
    """Make quest for user.

    Returns:
        String when says what user own do.
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def try_count():
    """Tryes in even game.

    Returns:
        Number of tryes.
    """
    return 3


def game_stats():
    """Stats of game.

    Returns:
        Number for operation and right answer 'yes' or 'no' for even game.
    """
    num_for_quest = random.randint(1, 100)
    right_answer = "no" if num_for_quest % 2 else "yes"
    return f"{num_for_quest}", right_answer
