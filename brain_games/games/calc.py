#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn


def calc(user_name):
    i = 0
    while i < games_ctn:
        rnd_number_a = randint(1, 99)
        rnd_number_b = randint(1, 99)
        rnd_number_action = randint(1, 3)
        if rnd_number_action == 1:
            rnd_number_action = '+'
            result = rnd_number_a + rnd_number_b
        elif rnd_number_action == 2:
            rnd_number_action = '-'
            result = rnd_number_a - rnd_number_b
        elif rnd_number_action == 3:
            rnd_number_action = '*'
            result = rnd_number_a * rnd_number_b

        qst_text = 'Question: {} {} {}'
        print(qst_text.format(rnd_number_a, rnd_number_action, rnd_number_b))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(result):
            print('Correct!')
            i += 1
        else:
            wrng_msg = '\'{}\' is wrong answer ;(. Correct answer was \'{}\'.\n'
            wrng_text = wrng_msg.format(user_answer, result)
            try_again_text = 'Let\'s try again, {}!'.format(user_name)
            return print(wrng_text + try_again_text)
    return print('Congratulations, {}!'.format(user_name))
