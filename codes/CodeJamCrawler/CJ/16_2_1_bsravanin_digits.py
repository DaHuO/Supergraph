#! /usr/bin/env python
"""
Name: Sravan Bhamidipati
Date: 30th April, 2015
Purpose: https://code.google.com/codejam/contest/11254486/dashboard#s=p0
"""

import sys

key = {'0': list('ZERO'), '1': list('ONE'), '2': list('TWO'), '3': list('THREE'), '4': list('FOUR'), '5': list('FIVE'),
       '6': list('SIX'), '7': list('SEVEN'), '8': list('EIGHT'),'9': list('NINE')}


def filter(letters, digit):
    for x in digit:
        letters.remove(x)


def identify(letters, number):
    stop = False;
    if 'Z' in letters:
        filter(letters, key['0'])
        number.append('0')
    elif 'W' in letters:
        filter(letters, key['2'])
        number.append('2')
    elif 'U' in letters:
        filter(letters, key['4'])
        number.append('4')
    elif 'X' in letters:
        filter(letters, key['6'])
        number.append('6')
    elif 'G' in letters:
        filter(letters, key['8'])
        number.append('8')
    elif 'S' in letters:
        # Ruled out 6
        filter(letters, key['7'])
        number.append('7')
    elif 'V' in letters:
        # Ruled out 7
        filter(letters, key['5'])
        number.append('5')
    elif 'T' in letters:
        # Ruled out 2, 8
        filter(letters, key['3'])
        number.append('3')
    elif 'O' in letters:
        # Ruled out 0, 2, 4
        filter(letters, key['1'])
        number.append('1')
    elif 'N' in letters:
        # Ruled out 1, 7
        filter(letters, key['9'])
        number.append('9')
    else:
        stop = True

    return stop


def word_to_number(word):
    number = []
    letters = list(word)
    while True:
        if identify(letters, number):
            return ''.join(sorted(number))


with open(sys.argv[1]) as fd:
    for line_no, line in enumerate(fd):
        if line_no == 0:
            continue
        else:
            print 'Case #%s: %s' % (line_no, word_to_number(line.strip()))
