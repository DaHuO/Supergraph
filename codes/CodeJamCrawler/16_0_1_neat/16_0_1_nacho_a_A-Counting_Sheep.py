#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from sys import argv

def count_sheep(n):
    if int(n) == 0: # Finishes for every other n < 10^6 (checked exhaustively)
        return "INSOMNIA"
    else:
        digits = set()
        i = 1
        next_n = 0
        while len(digits) < 10:
            next_n = str(int(n) * i)
            digits |= set(next_n)
            i+=1
        return next_n



if __name__ == "__main__":
    if len(argv) < 2:
        print "Error\nUsage: " + argv[0] + " input_file"
        quit()

    test_cases = open(argv[1], "r").read().split("\n")
    for i in range(1, len(test_cases)): # Skip first line
        n = test_cases[i]
        if n != '':
            print "Case #" + str(i) + ": "+ count_sheep(n)
