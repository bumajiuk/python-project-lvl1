#!/usr/bin/env python
from random import randint
import prompt
from brain_games.games.settings import games_ctn


def calc(user_name):
    i = 0
    while i < games_ctn:
        random_number_a = randint(1, 99)
        random_number_b = randint(1, 99)
        random_number_action = randint(1, 3)
        if random_number_action == 1:
            random_number_action = '+'
            result = random_number_a + random_number_b
        elif random_number_action == 2:
            random_number_action = '-'
            result = random_number_a - random_number_b
        elif random_number_action == 3:
            random_number_action = '*'
            result = random_number_a * random_number_b

        print('Question: {} {} {}'.format(random_number_a, random_number_action, random_number_b))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(result):
            print('Correct!')
            i += 1
        else:
            wrong_text = '\'{}\' is wrong answer ;(. Correct answer was \'{}\'.\n'.format(user_answer, result)
            try_again_text = 'Let\'s try again, {}!'.format(user_name)
            return print(wrong_text + try_again_text)
    return print('Congratulations, {}!'.format(user_name))
