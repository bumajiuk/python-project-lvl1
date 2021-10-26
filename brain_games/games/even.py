#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn


def even(user_name):
    i = 0
    while i < games_ctn:
        random_number = randint(1, 99)
        print('Question: {}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if ((random_number % 2) == 0) and (user_answer == 'yes'):
            print('Correct!')
            i += 1
        elif (random_number % 2) != 0 and user_answer == 'no':
            print('Correct!')
            i += 1
        else:
            return print('Let\'s try again, {}!'.format(user_name))
    return print('Congratulations, {}!'.format(user_name))
