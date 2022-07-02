"""File with game."""
import random


def make_quest():
    """Make quest for user.

    Returns:
        String when says what user own do.
    """
    return 'What is the result of the expression?'


def try_count():
    """Tryes in even game.

    Returns:
        Number of tryes.
    """
    return 3


def random_number():
    return random.randint(1, 25)


def summ(number1, number2):
    return number1 + number2


def minus(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def game_stats():
    """Stats of game.

    Returns:
        Number for operation and right answer 'yes' or 'no' for even game.
    """
    option_mass = ['+', '-', '*']
    option = random.choice(option_mass)
    if option == '+':
        number1 = random_number()
        number2 = random_number()
        right_answer = number1 + number2
        return f"{number1} + {number2}", f"{right_answer}"
    elif option == '-':
        number1 = random_number()
        number2 = random_number()
        right_answer = number1 - number2
        return f"{number1} - {number2}", f"{right_answer}"
    elif option == '*':
        number1 = random_number()
        number2 = random_number()
        right_answer = number1 * number2
        return f"{number1} * {number2}", f"{right_answer}"
