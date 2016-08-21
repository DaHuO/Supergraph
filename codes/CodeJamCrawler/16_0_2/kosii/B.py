from itertools import *
from functools import *
from operator import *
from math import *
from collections import Counter

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

filename = "B-large"
result_string = "Case #{}: {}"

def invert(pattern):
    return "".join(["+" if (i == "-") else "-" for i in pattern])

def flip(pattern, n):
    return invert(pattern[:n])[::-1] + pattern[n:]

def calc(pattern, every=True):
    if set(pattern) == set("-"):
            return 1
    if set(pattern) == set("+"):
        return 0

    if every:
        r = xrange(1, len(pattern) + 1)
    else:
        r = xrange(1, len(pattern))
    for i in r:
        print flip(pattern, i)
        # calc(flip(pattern, i), i == len(pattern))

def main(input_filename, output_filename):
    with open(input_filename) as input, open(output_filename, 'w') as output:
        T, = nis(input)
        for t in range(T):
            S, = sis(input)
            # print "orig", S
            endswith = S[-1]
            res = len(filter(lambda (a, b): a != b, zip(S, S[1:])))
            if endswith != '+':
                res += 1
            w(output, t, res)


def w(output, i, res):
    print result_string.format(i+1, res)
    output.write(result_string.format(i+1, res)+'\n')

def sis(input):
    return input.readline().split()

def nis(input):
    return map(int, input.readline().split())

def integer_sqrt(i):
    """return tuple (s, b), where b is true if and only if i is a perfect square
    and s is the integer square root
    """
    if not i: return 0
    if i < 0: raise ValueError("cannot calculate square root of negative")
    def n(xn):
        return (xn + i/xn)/2
    xn, xnp, xnpp = i, n(i), n(n(i))
    while xn != xnpp:
        xn, xnp, xnpp = xnp, xnpp, n(xnpp)
    return min(xnp, xnp)

class Memoize(object):
    def __init__(self, f):
        self.f = f
        self.memory = {}
    def __call__(self, *args, **kwargs):
        if (tuple(args), tuple(kwargs.items())) in self.memory:
            return self.memory[(tuple(args), tuple(kwargs.items()))]
        else:
            val = self.f(*args, **kwargs)
            self.memory[(tuple(args), tuple(kwargs.items()))] = val
            return val


if __name__ == '__main__':
    input_filename = "{}.in".format(filename)
    output_filename = "{}.out".format(filename)
    main(input_filename, output_filename)
