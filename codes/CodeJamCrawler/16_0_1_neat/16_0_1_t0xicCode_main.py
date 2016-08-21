from __future__ import print_function
import itertools

def output(n):
    if n is 0:
        return "INSOMNIA"

    digits = set()
    for i in itertools.count(1):
        w = i * n
        for d in str(w):
            digits.add(d)

        if len(digits) is 10:
            return str(w)

num = int(raw_input())

for i in range(0, num):
    print(''.join(["Case #", str(i+1), ": ", output(int(raw_input()))]))
