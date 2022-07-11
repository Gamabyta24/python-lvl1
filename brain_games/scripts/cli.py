"""Client of game."""

import prompt


def get_user_name():
    """Get name of user.

    Returns:
        question(string):with your name
    """
    return prompt.string("May I have your name? ")


def hello_user(user_name):
    """Print hello username.

    Args:
        user_name(string): name 0f user.
    """
    print(f"Hello ,{user_name}!")


def print_message(message):
    """Print hello username.

    Args:
        message(string): message for user.
    """
    print(message)


def print_discr(discr):
    """Print point of game.

    Args:
        discr(string):discription of game.
    """
    print(discr)


def print_tryes(tryes):
    """Print your tryes.

    Args:
        tryes(int):tryes in game.
    """
    print("You tryes:", tryes)


def print_quest(number_for_quest):
    """Quest number for operation.

    Args:
        number_for_quest(string):print number for question.
    """
    print("Question:", number_for_quest)


def get_user_answer():
    """User input his answer here.

    Returns:
        word(string): yes or no
    """
    return input("Your answer: ")


def print_correct():
    """Print if user give correct answer."""
    print("Correct!")


def print_try_again():
    """Print if user give not correct answer."""
    print("Try again")


def print_win():
    """Print if user give 3 correct answer."""
    print("You win!")


def true_answer(right_answer, user_answer):
    """Print right answer and user answ.

    Args:
        right_answer(string): true answer
        user_answer(string): answer from user
    """
    print(f"'{user_answer}' is wrong answer ;( Correct answer was '{right_answer}'.")
