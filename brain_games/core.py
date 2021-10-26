#!/usr/bin/env python
from brain_games.welcome import welcome_user
from brain_games.games.settings import brain_even, no_game
from brain_games.games.even import even


def core(game_name):
    user_name = welcome_user()
    if game_name == 'brain_even':
        print(brain_even)
        even(user_name)
    elif game_name == 'brain_calc':
        print(brain_even)
    #    brain_calc(user_name)
    else:
        print(no_game)
