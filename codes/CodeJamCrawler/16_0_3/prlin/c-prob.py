from __future__ import print_function
import sys
import math
import random

def bit_perms(n):
    # 2**(n-2) possibilities
    a = '{0:0%sb}' % (n-2)
    for i in xrange(0, 2**(n-2)):
        mid = a.format(i)
        yield '1'+mid+'1'


def fast_mod(a,b,c):
    x,y = 0,a%c
    while b>0:
        if b%2==1:
            x= (x*y)%c
        y = (y*2)%c
        b /=2
    return x%c

prime_mem = {2: (True, 0)}
def check(int_n):
    '''
    miller-rabin -> is this prime? if so (True, _)
    if not (False, factor)
    '''
    if int_n < 2:
        return True, 0

    if int_n in prime_mem:
        return prime_mem[int_n]

    if int_n != 2 and int_n%2==0:
        prime_mem[int_n] = (False, 2)
        return False, 2

    p = int_n
    for _ in xrange(2):  # change for accuracy
        a = random.randint(2, p-1)
        print('\tchecking a:{} and p:{}'.format(a, p), file=sys.stderr)
        if (fast_mod(a, p-1, p) != 1):
            # definitely not prime
            # find a factor
            if p % 3 == 0:
                return False, 3
            else:
                i=5
                count = 0
                while i*i < p and count < 100:  # takes forever to find sometimes
                    print('\tfinding factor: i:{} p:{}'.format(i, p), file=sys.stderr)
                    if p%i==0:
                        prime_mem[int_n] = (False, i)
                        return False, i
                    elif p%(i+2)==0:
                        prime_mem[int_n] = (False, i+2)
                        return False, i+2
                    i+=6
                    count += 1

    prime_mem[int_n] = (True, 0)
    return True, 0

def handle_case(line):
    N, J = [int(x) for x in line.strip().split(' ')]
    output = []

    # yield N string permutation
    perms = bit_perms(N)

    j = 0
    while j < J:
        try:
            n = next(perms)
            print('trying n: %s %s'% (int(n, 2), n) , file=sys.stderr)
            divs = []
        except StopIteration:
            print('DONE WITH ALL NUMBERS', file=sys.stderr)
            return
        for base in xrange(2, 11):
            int_n = int(n, base)
            print('\tprime check n:%s base:%s'% (int_n, base) , file=sys.stderr)
            prime, div = check(int_n)
            if prime:
                break
            else:
                divs.append(str(div))
        else:
            j += 1
            output.append('\n')
            output.append('{} {}'.format(n, ' '.join(divs)))

    return ''.join(output)


if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        line = sys.stdin.readline().strip()
        answer = handle_case(line)
        print("Case #{}:{}".format(i, answer))
