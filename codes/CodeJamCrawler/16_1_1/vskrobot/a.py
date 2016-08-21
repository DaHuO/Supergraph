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
    result = []
    lines = input.read().splitlines()
    cases = int(lines[0])
    for i in xrange(1, cases + 1, 1):
        letters = list(lines[i])

        words = {}
        for j in xrange(0, len(letters)):
            words[j] = []
            letter = letters[j]
            if j == 0:
                words[j] = list(letter)
            else:
                for w in xrange(0, len(words[j-1])):
                    temp = words[j-1][w]
                    if not isinstance(temp, list):
                        temp = list(temp)

                    words[j].append(temp + list(letter))
                    words[j].append(list(letter) + temp)


        res = map(''.join,words[len(letters) - 1])
        res.sort()
        result.append('Case #' + str(i) + ': ' + res[-1])

    return "\n".join(result)


if os.path.isfile('input.in'):
    run('input.in')

if os.path.isfile('A-small-attempt0.in'):
    run('A-small-attempt0.in')

if os.path.isfile('A-large-practice.in'):
    run('A-large-practice.in')
