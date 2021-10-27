#!/usr/bin/env python
from brain_games.welcome import welcome_user
from brain_games.games.settings import brain_even, brain_calc
from brain_games.games.settings import brain_gcd, no_game
from brain_games.games.even import even
from brain_games.games.calc import calc
from brain_games.games.gcd import gcd


def core(game_name):
    user_name = welcome_user()
    if game_name == 'brain_even':
        print(brain_even)
        even(user_name)
    elif game_name == 'brain_calc':
        print(brain_calc)
        calc(user_name)
    elif game_name == 'brain_gcd':
        print(brain_gcd)
        gcd(user_name)
    else:
        print(no_game)
