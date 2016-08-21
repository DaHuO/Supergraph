__author__ = 'vskrobot'

import os.path
import math

def run(filename):
    """
    A helper function to run a testfile
    :param filename: A filename with input test data
    :return: None
    """
    input = open(filename, 'r')
    result = solution(input)
    output = open('output.' + filename, 'w')
    output.write(result)

def prime_number(number):
    if number <= 1:
        return False

    saturation = int(math.sqrt(number)) + 1

    for i in xrange(2, saturation):
        if number % i == 0:
            return False

    return True

def divisor(number, values):
    if number <= 1:
        return False

    saturation = int(math.sqrt(number)) + 1

    for i in xrange(2, saturation):
        if number % i == 0:
            if i in values:
                continue
            else:
                return i

    return False


def solution(input):
    """
    A main function to solve a task
    :param input: Input data
    :return: text with output
    """
    lines = input.read().splitlines()
    cases = int(lines[0])
    result = []

    for i in xrange(1, cases + 1, 1):
        result.append('Case #' + str(i) + ':')
        length, required = map(int, lines[i].split(' '))
        jamcoins_dict = {}
        jamcoins = []

        coins_first = ''.join(['1'] + (['0'] * (length - 2)) + ['1'])
        coins_last = ''.join(['1'] * length)

        for coin in xrange(int(coins_first, 2), int(coins_last, 2) + 1):
            jamcoin = str('{0:b}'.format(coin))
            valid = True
            temp = []
            values = []

            if jamcoin.endswith('0'):
                continue

            for base in xrange(2, 11):
                value = int(jamcoin, base)

                if not prime_number(value):
                    values.append(value)
                else:
                    valid = False
                    break

            if not valid:
                continue

            for value in values:
                temp.append(str(divisor(value, values)))

            jamcoins.append(jamcoin)
            jamcoins_dict[jamcoin] = temp

            if len(jamcoins) > required:
                break

    for j in xrange(0, required):
        if j >= len(jamcoins):
            break

        result.append(jamcoins[j] + ' ' + ' '.join(jamcoins_dict[jamcoins[j]]))

    return "\n".join(result)


if os.path.isfile('input.in'):
    run('input.in')

if os.path.isfile('C-small-attempt0.in'):
    run('C-small-attempt0.in')

if os.path.isfile('C-large-practice.in'):
    run('C-large-practice.in')
