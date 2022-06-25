import prompt
def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,{name}!")


def get_user_name():
    return prompt.string('May I have your name? ')

def hello_user(user_name):
    print(f'Hello ,{user_name}!')

def print_message(message):
    print(message)

def print_discr(discr):
    print(discr)

