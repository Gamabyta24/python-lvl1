"""File with game."""
import random


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
    option_mass = ["+", "-", "*"]
    option = random.choice(option_mass)
    if option == "+":
        right_answer = summ(number1, number2)
        return f"{number1} + {number2}", f"{right_answer}"
    elif option == "-":
        right_answer = minus(number1, number2)
        return f"{number1} - {number2}", f"{right_answer}"
    elif option == "*":
        right_answer = multiplication(number1, number2)
        return f"{number1} * {number2}", f"{right_answer}"
