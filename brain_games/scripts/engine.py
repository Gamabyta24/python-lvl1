import prompt

from brain_games.global_const import MESSAGE



def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,{name}!")


def run(game, cli):
    cli.print_message(MESSAGE)
    user_name = cli.get_user_name()
    cli.hello_user(user_name)
    cli.print_discr(game.make_quest())
    tryes = game.try_count()
    print("You tries", tryes)
    for _ in range(tryes):
        num, right_answer = game.even()
        print("Question:", num)
        user_answer = input("Your answer: ")
        if user_answer == right_answer:
            print("Correct")
        else:
            print("Try again")
            return
    print("Congrats")
