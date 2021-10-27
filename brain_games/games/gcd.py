#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn
import math


def gcd(user_name):
    i = 0
    while i < games_ctn:
        rnd_nmb_a = randint(1, 99)
        rnd_nmb_b = randint(1, 99)
        correct_answer = math.gcd(rnd_nmb_a, rnd_nmb_b)
        print('Question: {} {}'.format(rnd_nmb_a, rnd_nmb_b))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            i += 1
        else:
            wrng_msg = '\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'
            wrng_txt = wrng_msg.format(user_answer, correct_answer)
            retry_txt = '\nLet\'s try again, {}!'.format(user_name)
            return print(wrng_txt + retry_txt)
    return print('Congratulations, {}!'.format(user_name))
