#!/usr/bin/env python
import fileinput
import sys
import itertools


def main():
    out_tpl = 'Case #{}: {}\n'
    case_num = -1
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
    else:
        fname = None

    for idx, line in enumerate(fileinput.input(fname)):
        if idx == 0:
            case_num = int(line.strip())
        else:
            print 'Case #%s:' % idx
            N, J =line.split()
            n = int(N)
            j = int(J)
            solve(n, j)


def str_to_n(s, base):
    ret = 0
    for idx, ch in enumerate(reversed(s)):
        ret += base ** idx * int(ch)

    return ret

def output(num, facts):
    lst = [num] + facts
    lst2 = [str(i) for i in lst]
    sys.stdout.write(' '.join(lst2))
    sys.stdout.write('\n')
    sys.stdout.flush()

def solve(n, j):
    repeat = n - 2
    # '01' make sure it is in order
    for p in itertools.product('01', repeat=repeat):
        num = '1{}1'.format(''.join(p))
        facts = []
        is_jcoin = True
        for base in xrange(2, 11):
            num1 = str_to_n(num, base)
            is_p, fact = is_prime(num1)
            if is_p:
                is_jcoin = False
                break
            else:
                facts.append(fact)
        if is_jcoin:
            output(num, facts)
            j-=1
            if j == 0:
                return


def is_prime(n):
    '''check if integer n is a prime'''

    # all other even numbers are not primes
    if n < 2:
        return False, None
    # 2 is the only even prime number
    if n == 2: 
        return True, None
 
    if not n & 1: 
        return False, 2

    n_str = str(n)
    if n_str[-1] in ('5', '0'):
        return False, 5

    # 0 and 1 are not primes
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in xrange(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False, x
    return True, None

if __name__ == '__main__':
    main()
