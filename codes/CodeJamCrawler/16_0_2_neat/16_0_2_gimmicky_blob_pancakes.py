#! /usr/bin/python

import sys

def invert(x):
    if x == "+":
        return "-"
    else:
        return "+"

def flip(sequence):
    return "".join(map(invert, reversed(sequence)))
    

def minimum_flips(sequence):
    if len(sequence) == 1:
        if sequence[0] == '+':
            return 0
        else:
            return 1
    else:
        if sequence[-1] == '+':
            return minimum_flips(sequence[0:-1])
        elif (sequence[0], sequence[-1]) == ('-', '-'):
            return 1 + minimum_flips(flip(sequence)[0:-1])
        elif (sequence[0], sequence[-1]) == ('+', '-'):
            i = 0
            while sequence[i] == '+':
                i+= 1
                
            return 2 + minimum_flips(flip(sequence)[0:-i])
        else:
            raise "Unexpected Sequence"

if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    for test_number in range(1, num_tests + 1):
        sequence = sys.stdin.readline().strip()
        print("Case #{}: {}".format(test_number, minimum_flips(sequence)))