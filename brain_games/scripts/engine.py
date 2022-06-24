import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,{name}!")


def run(x, cli):
    cli()
    print(x.make_quest())
    tryes = x.try_count()
    print("You tries", tryes)
    for _ in range(tryes):
        num, right_answer = x.even()
        print("Question:", num)
        user_answer = input("Your answer: ")
        if user_answer == right_answer:
            print("Correct")
        else:
            print("Try again")
            return
    print("Congrats")
