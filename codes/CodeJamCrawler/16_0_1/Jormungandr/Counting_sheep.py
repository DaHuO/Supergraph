#!/usr/bin/env python

__author__ = 'Bill'

from misc import input_, output_

num_cases, cases = input_('A-large.in')

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
answers = []


for case in cases:
    case = case.rstrip('\n')
    done = False
    if case == '0':
        answers.append('INSOMNIA')
        done = True
    while done == False:
        seen = set()
        for ch in case:
            seen.add(ch)
        if seen.intersection(digits) == digits:
            answers.append(case)
            done = True
        i = 2
        while done == False:
            number = int(case) * i
            i += 1
            for ch in str(number):
                seen.add(ch)
            if seen.intersection(digits) == digits:
                answers.append(number)
                done = True

output_(answers, 'Counting_sheep_large.out')



