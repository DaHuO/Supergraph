#!/usr/bin/env python

def put_digit(no, digit_set):
    while no > 0:
        digit = no % 10
        no = no / 10
        digit_set.add(digit)
    return len(digit_set)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, o, digit_set = int(raw_input()), "", set()
    if n == 0:
        o = "INSOMNIA"
    else:
        for x in range(n, n*200, n):
            if put_digit(x, digit_set) == 10:
                o = x
                break
        else:
            o = "INSOMNIA"
    print "Case #{}: {}".format(i, o)

