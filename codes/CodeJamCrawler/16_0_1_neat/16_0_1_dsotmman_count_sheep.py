#!/usr/bin/env python

from __future__ import print_function

def soln(case, n):
    digit_set = set()
    # only in this case can we never fall asleep
    if n == 0:
        print("CASE #{}: INSOMNIA".format(case + 1))
        return

    i = 1
    while True:
        digit_set.update(j for j in str(i*n))
        if len(digit_set) == 10:
            print("CASE #{}: {}".format(case + 1, i*n))
            return
        i += 1


if __name__=='__main__':
    T = int(raw_input())
    for i in range(T):
        n = int(raw_input())
        soln(i, n)
