#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn


def is_prime(number):
    """Check if number is prime or not."""
    if number < 2 or not number % 2:
        return False
    counter = 3
    while counter <= number // 2:
        if not number % counter:
            return False
        counter += 2
    return True


def prime(user_name):
    i = 0
    while i < games_ctn:
        a = randint(2, 3572)
        answer = is_prime(a)
        print('Question: {}'.format(a))
        user_answer = prompt.string('Your answer: ')
        if (answer == True) and (user_answer == 'yes'):
            print('Correct!')
            i += 1
        elif (answer == False) and (user_answer == 'no'):
            print('Correct!')
            i += 1
        else:
            retry_txt = 'Let\'s try again, {}!'.format(user_name)
            return print(retry_txt)
    return print('Congratulations, {}!'.format(user_name))
