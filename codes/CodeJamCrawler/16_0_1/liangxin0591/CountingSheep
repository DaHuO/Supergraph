#!/usr/bin/python

import sys


# N is an integer
def countingSheep(N):
    digits = {}
    numbers = {}
    count = 0
    base = N
    while (not (numbers.has_key(N))):
        numbers[N] = 1
        count = count + 1
        M = N
        while (M / 10 > 0):
            digits[M % 10] = digits.get(M % 10, 0) + 1
            M = M / 10

        digits[M % 10] = digits.get(M % 10, 0) + 1
        #print N
        #print digits.keys()
        if (len(digits.keys()) == 10):
            return count
        else:
            N = N + base
    return 0


if __name__ == "__main__":
    
    t = int(raw_input()) # read a line with single integer
    for i in range(1, t + 1):
        N = int(raw_input())
        count = countingSheep(N)
        if (count == 0):
            print("Case #" + str(i) + ": INSOMNIA")
        else:
            print("Case #" + str(i) + ": " + str(count*N))
