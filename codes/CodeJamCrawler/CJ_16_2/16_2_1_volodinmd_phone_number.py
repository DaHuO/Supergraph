from __future__ import print_function
__author__ = 'volodin'

import re

prime = {'Z': ('ZERO', 0), 'W': ('TWO', 2), 'U': ('FOUR', 4), 'X': ('SIX', 6), 'G': ('EIGHT', 8)}
secondary = {'O': ('ONE', 1), 'T': ('THREE', 3), 'F': ('FIVE', 5), 'S': ('SEVEN', 7)}

def replace(line, word):
    for char in word:
        line = line.replace(char, '', 1)
    return line


def solve(line):
    digits = []

    while line:
        foundAny = False
        for letter, pair in prime.iteritems():
            if letter in line:
                foundAny = True
                digits.append(pair[1])
                line = replace(line, pair[0]) #re.sub("[{0}]".format(pair[0]), '', line)
                if not line:
                    break
        if not foundAny:
            break

    while line:
        foundAny = False
        for letter, pair in secondary.iteritems():
            if letter in line:
                foundAny = True
                digits.append(pair[1])
                line = replace(line, pair[0]) #re.sub("[{0}]".format(pair[0]), '', line)
                if not line:
                    break
        if not foundAny:
            break

    #check nines
    while line:
        digits.append(9)
        line = replace(line, "NINE")

    return sorted(digits)


input = open('numbers.in', 'r')
output = open('numberout.txt', 'w')
T = input.readline()
for i in range(0, int(T)):
    answer = solve(input.readline().rstrip('\r\n'))
    stringlist = ''.join(str(v) for v in answer)
    answer = "Case #{0}: {1}\n".format(i + 1, stringlist)
    print(answer, end='')
    output.write(answer)
