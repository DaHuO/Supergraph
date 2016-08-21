#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from sys import argv
from math import sqrt

# Returns 0 if n is prime and the smallest not trivial divisor of n otherwise
def smallest_divisor(n):
    for i in xrange(3, int(sqrt(n)) + 1):
        if (i > 100000): # Takes too long. Consider it prime and try another
            return 0
        if (n % i == 0):
            return i
    return 0


def interpret_in_base(number, base):
    value = 0
    for digit in xrange (1, len(number) + 1):
        value += int(number[-digit]) * (base ** (digit - 1))
    return value

def is_jamcoin(number):
    divisors = ""
    for base in xrange(2, 11):
        divisor = smallest_divisor(interpret_in_base(number,base))
        if divisor == 0:
             return ""
        else:
            divisors += " " + str(divisor)
    return divisors

def find_jamcoins(n, j):
    jamcoins_found = 0
    format_string = "1{:0" + str(n-2) + "b}1"
    for i in xrange(0, 2 ** (n-2)):
        jamcoin_candidate = format_string.format(i)
        divisors = is_jamcoin(jamcoin_candidate)
        if divisors != "":
            jamcoins_found +=1
            print jamcoin_candidate + divisors
        if jamcoins_found >= j:
            break


if __name__ == "__main__":
    if len(argv) < 2:
        print "Error\nUsage: " + argv[0] + " input_file.in"
        quit()

    test_cases = open(argv[1], "r").read().split("\n")
    for i in range(1, len(test_cases)): # Skip first line
        test_case = test_cases[i]
        if test_case != "":
            print "Case #" + str(i) + ":"
            n_j = test_case.split(" ")
            find_jamcoins(int(n_j[0]), int(n_j[1]))
