__author__ = 'lowikchanussot'

from math import sqrt

def isPrime(n):
    if n < 2: return False, 1
    for number in xrange(2, int(sqrt(n))+1):
        if not n%number:
            return False, number
    return True, 1

def is_solution(p):
    divisors = []
    for b in xrange(2, 11):
        nb = int(p, base=b)
        prime, d = isPrime(nb)
        if not prime:
            divisors.append(d)
        else:
            return False, []
    return True, divisors

def gen_potential_jamcoin16():
    for i in xrange(2**15 + 1, 2**16 - 1, 2):
        yield '{:016b}'.format(i)


def get_solutions_16(J):
    solutions = []
    for p in gen_potential_jamcoin16():
        ok, ds = is_solution(p)
        if ok:
            solution = p + ' ' + ' '.join([str(d) for d in ds])
            solutions.append(solution)
            if len(solutions) == J:
                return solutions


def solveC_small(out_filename):
    with open(out_filename, 'w') as ofile :
        solutions = get_solutions_16(50)
        ofile.write("Case #1: \n")
        ofile.write('\n'.join(solutions))


if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '_out'
    solveC_small(output)