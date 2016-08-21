from __future__ import division
from collections import Counter
import itertools
import math


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


# def multiple_output(n, fun):
#     for i in xrange(n):
#         write_output(i + 1, fun(lines[i + 1]))

dictionary = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def if_digit_in_string(digit, string, i):
    # if string is '':
        # return i, ''
    newstr = string
    for ch in digit:
        if ch not in newstr:
            return i, string
        newstr = update_string(ch, newstr)
    i+=1
    # if newstr:
    i, newstr = if_digit_in_string(digit, newstr, i)
    # else:
    return i, newstr



def update_string(digit, string):
    newstr = string
    for ch in digit:
        newstr = newstr.replace(ch, "", 1)
    return newstr


def find_numbers(string):
    number = ''
    newstr = string
    for j, d in enumerate(dictionary):
        i, newstr = if_digit_in_string(d, newstr,0)
        number += i*str(j)
    if newstr:
        newstr = string
        number = ''
        for j, d in enumerate(reversed(dictionary)):
            i, newstr = if_digit_in_string(d, newstr,0)
            number += i*str(9-j)
    return ''.join(sorted(number))


if __name__ == '__main__':
    lines = read_file("A3.in")
    for n in xrange(0, int(lines[0])):
    # n = 98
        string = lines[n + 1]
        print("Case #%d: %s" % (n + 1, find_numbers(string)))

