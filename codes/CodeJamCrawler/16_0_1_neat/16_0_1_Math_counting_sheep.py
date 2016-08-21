#!/usr/bin/env python3
#-*- coding: utf8 -*-
import sys

def sheep_count(NN, count):
    count_string = "Case #" + str(count) + ": "
    ii = 1
    digits_seen = list()
    prev_len = 0
    if (NN == 0):
        print(count_string + "INSOMNIA")
        return
    while (True):
        number = ii * NN
        ii += 1
        for digit in str(number):
            if (not digit in digits_seen):
                digits_seen.append(digit)
        if (len(digits_seen) == 10):
            print(count_string + str(number))
            return

if __name__ == "__main__":
    TT = int(input())
    for ii in range(TT):
        sheep_count(int(input()), ii+1)

