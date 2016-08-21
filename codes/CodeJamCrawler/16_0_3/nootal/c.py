#!/usr/bin/env pypy
import sys
import os

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        if (n % d) == 0:
            return d
        d += 1

outfile = open("%s.out" % sys.argv[1], "w")

def format_result(index):
    return "Case #{}:".format(index + 1)

from math import pow

def check_base(s):
    denominators = list()
    for base in range(2, 11):
        based_value = int(s, base)
        p = primes(based_value) 
        if p == None:
            return
        denominators.append(p)
    return denominators

def solving(index, input):
    N, J = input
    output = format_result(index)
    count = 0
    n = int(N)
    # for i in range(int(pow(2, n))):
    for i in range(int(pow(2, n)) / 2 + 1, int(pow(2, n)), 2):
        s = format(i, 'b')
        s = "0" * (n - len(s)) + s
        print("Trying {}...".format(s))
        c = check_base(s)
        if c == None:
            continue
        print("\tOK")
        output += '\n{} '.format(s) + " ".join(map(lambda x: str(x), c))
        count += 1
        if count == int(J):
            break
    print
    print(output)
    outfile.write(output)

with open(sys.argv[1]) as infile:
    case = []
    for index, l in enumerate(infile.readlines()[1:]):
        N, J = l.strip().split()
        solving(index, (N, J))
    
outfile.close()
