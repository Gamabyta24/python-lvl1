import random


def make_quest():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def try_count():
    return 3


def even():
    num_for_quest = random.randint(1, 100)
    right_answer = "no" if num_for_quest % 2 else "yes"
    return f"{num_for_quest}", right_answer
