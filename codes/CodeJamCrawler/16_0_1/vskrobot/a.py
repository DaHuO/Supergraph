__author__ = 'vskrobot'

import os.path


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


def solution(input):
    """
    A main function to solve a task
    :param input: Input data
    :return: text with output
    """
    output = []

    lines = input.read().splitlines()
    cases = int(lines[0])

    for i in xrange(1, cases + 1, 1):
        digits = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}

        number = lines[i]
        if number == '0':
            output.append('Case #' + str(i) + ': INSOMNIA')
            continue

        mult = 1
        while digits:
            value = str(int(number) * mult)
            for char in xrange(0, len(value)):
                if value[char] in digits:
                    digits.pop(value[char])
            mult += 1
            result = value

        output.append('Case #' + str(i) + ': ' + result)

    return "\n".join(output)


if os.path.isfile('input.in'):
    run('input.in')

if os.path.isfile('A-small-attempt0.in'):
    run('A-small-attempt0.in')

if os.path.isfile('A-large.in'):
    run('A-large.in')
