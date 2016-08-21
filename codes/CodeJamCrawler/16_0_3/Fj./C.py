import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob
import itertools

taskname = 'C'
input_file = None

input_file = None

def readstr():
    return next(input_file).strip()

def readintlist():
    lst = list(map(int, readstr().split()))
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]


def numbers(n):
    for s in itertools.product([1], *([[0, 1]] * (n - 2)), [1]):
        yield s
        

def to_base(lst, base):
    acc = 0
    power = 1
    for i in reversed(lst):
        acc += i * power
        power *= base
    return acc 


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = rwh_primes(10000)
print(len(primes))

def all_divisors(n):
    r = []
    for prime in primes:
        while n % prime == 0:
            r.append(prime)
            n /= prime
            if n == 0: return r
    return r

def solvecase():
    N, J = readintlist()
    bases = list(reversed(range(2, 11)))
    generated = 0
    divisors = [None] * 11
    result = '\n' 
    for n in numbers(N):
        for base in bases:
            n_base = to_base(n, base)
            for prime in primes:
                if n_base % prime == 0:
                    divisors[base] = prime
                    break
            else:
                # possibly prime
                break
        else:
            # all bases OK.
#              print(''.join(str(c) for c in n), ':', ' '.join(repr(all_divisors(to_base(n, base))) for base in range(2, 11))) 
            result += ''.join(str(c) for c in n) + ' ' + ' '.join(str(divisors[i]) for i in range(2, 11)) + '\n'
            generated += 1
            if generated >= J:
                break
    return result


def solve(input_name, output_name):
    global input_file
    tstart = time.clock()
    with open(input_name, 'r') as input_file, open(output_name, 'w') as output_file:
        casecount = readint()
        
        for case in range(1, casecount + 1):
            s = solvecase()
            s = "Case #%d: %s" % (case, str(s)) 
            print(s, file=output_file)
            print(s) 
        
    print('%s solved in %.3f' % (input_name, time.clock() - tstart))
def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
