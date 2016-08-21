import math

# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers

import random
_mrpt_num_trials = 5 # number of bases to test

def is_probable_prime(n):
    assert n >= 2
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True


def to_base(n, base):
    ret, power = 0, 1
    while n:
        ret += (n & 1) * power
        n >>= 1
        power *= base
    return ret


def is_prime(n):
    if n == 1: return None
    
    for ch in range(2, min(int(math.floor(math.sqrt(n))) + 1, 10**4)):
        if n % ch == 0:
            return ch
    return None


out = open("output.txt", 'w')
class Solver:
    def __init__(self, n, NUM):
        self.n = n
        self.NUM = NUM
        self.done = 0
        self.checked = set()
    
    def check(self, candidate):
        if not (candidate & 1): return
        
        if candidate in self.checked:
            return
        self.checked.add(candidate)
        
        curr = []
        for base in range(2, 11):
            in_base = to_base(candidate, base)
            if is_probable_prime(in_base):
                return
    
            cert = is_prime(in_base)
    
            if cert:
                curr.append(str(cert))
            else:
                return
    
        if len(curr) == 9:
            out.write(bin(candidate)[2:] + ' ' + ' '.join(curr) + '\n')
    
            self.done += 1
            print(self.done, bin(candidate)[2:])
            
        
        if self.done == self.NUM:
            out.close()
            exit(0)


random.seed(218 ** 2)

import sys

def main(n, NUM):
    out.write('Case #1:\n')
    
    found = 0
    
    start, end = 1 << (n - 1), 1 << n
    
    solver = Solver(n, NUM)
    for i in range(start, end):
        solver.check(i)

    return False


print(main(32, 500))