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


def flip(stack, position):
    position += 1
    top = list(stack[0:position])
    bottom = stack[position:]

    for i, cake in enumerate(top):
        if top[i] == '-':
            top[i] = '+'
        else:
            top[i] = '-'

    return "".join(top) + bottom


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
        stack = lines[i]
        movements = 0
        for position in xrange(0, len(stack)):
            position = len(stack) - position - 1
            pancake = stack[position]
            if pancake == '-':
                stack = flip(stack, position)
                movements += 1

        result.append('Case #' + str(i) + ': ' + str(movements))

    return "\n".join(result)


if os.path.isfile('input.in'):
    run('input.in')

if os.path.isfile('B-small-attempt0.in'):
    run('B-small-attempt0.in')

if os.path.isfile('B-large.in'):
    run('B-large.in')
