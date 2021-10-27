#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn


def progression(user_name):
    i = 0
    while i < games_ctn:
        rnd_nmb_a = randint(1, 99)
        rnd_nmb_step = randint(1, 99)
        rnd_nmp_ctn = randint(5, 10)
        rnd_nmb_q = randint(5, rnd_nmp_ctn)
        j = 1
        number_temp = rnd_nmb_a
        string_q = ''
        while j <= rnd_nmp_ctn:
            if j == rnd_nmb_q:
                string_q = string_q + '.. '
                correct_answer = number_temp
                number_temp = number_temp + rnd_nmb_step
                j += 1
            else:
                string_q = string_q + str(number_temp) + ' '
                number_temp = number_temp + rnd_nmb_step
                j += 1

        print('Question: {}'.format(string_q))
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
