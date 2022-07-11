"""File with game."""
import random
from operator import add, mul, sub


def make_quest():
    """Make quest for user.

    Returns:
        String when says what user own do.
    """
    return "What is the result of the expression?"


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
    return random.randint(1, 25)


def summ(number1, number2):
    """Summ two nums.

    Args:
        number1(int):number for operation.
        number2(int):number for operation.

    Returns:
        result of expression.
    """
    return number1 + number2


def minus(number1, number2):
    """Minus two nums.

    Args:
        number1(int):number for operation.
        number2(int):number for operation.

    Returns:
        result of expression.
    """
    return number1 - number2


def multiplication(number1, number2):
    """Multi two nums.

    Args:
        number1(int):number for operation.
        number2(int):number for operation.

    Returns:
        result of expression.
    """
    return number1 * number2


def game_stats():
    """Stats of game.

    Returns:
        Number for operation and right answer 'yes' or 'no' for even game.
    """
    number1 = random_number()
    number2 = random_number()
    pair_mass = [("+", add), ("-", sub), ("*", mul)]
    option = random.choice(pair_mass)
    operator_for_num, fuc_for_num = option
    right_answer = fuc_for_num(number1, number2)
    return f"{number1} {operator_for_num} {number2}", f"{right_answer}"
