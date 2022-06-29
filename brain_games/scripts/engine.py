"""Engine for launch all games in this project."""
from brain_games.global_const import MESSAGE


def run(game, cli):
    """Adaptive function for launch games.

    Args:
        game(module):file module with game.
        cli(module):file module with all outputs in terminal.
    """
    cli.print_message(MESSAGE)
    user_name = cli.get_user_name()
    cli.hello_user(user_name)
    cli.print_discr(game.make_quest())
    tryes = game.try_count()
    cli.print_tryes(game.try_count())
    for _ in range(tryes):
        number_for_quest, right_answer = game.game_stats()
        cli.print_quest(number_for_quest)
        user_answer = cli.get_user_answer()
        if user_answer == right_answer:
            cli.print_correct()
        else:
            cli.print_try_again()
            return
    cli.print_win()
