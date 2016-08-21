
import csv
import itertools
import copy
import time
import collections
import numpy as np


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L = csv_r.next()
        test_lst.append([int(e) for e in L])
    f.close() 
    return test_lst 


def get_divisor_lst_old(n):
    l=[e for e in xrange(2, n) if n%e==0]
    return l


def get_prime_lst(n_max):
    prime_lst=[]
    for e in xrange(2, n_max+1):
        if all([e%p!=0 for p in prime_lst]):
            prime_lst.append(e)
    return prime_lst

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def get_divisor_lst(n):
    for p in prime_lst:
        if p == n:
            break
        if n % p == 0:
            return [p]
        if p>n:
            break
    return []


def test_str(s):
    res=[]
    for i in xrange(2,11):
        n=int(s, i)
        l=get_divisor_lst(n)
        if len(l) == 0:
            return False, None
        res.append(min(l))
    return True, res


def get_all(n):
    if n == 0:
        return ['']
    res=[]
    for i in ['0', '1']:
        res.extend([i+e for e in get_all(n-1)])
    return res


def solve_test(test_case):
    N, J=test_case
    global prime_lst
    #prime_lst=get_prime_lst(10**N+1)
    prime_lst=primesfrom2to(10**6)
    prime_lst.sort()
    #print len(prime_lst)
    res=[]
    for i_e, e in enumerate(get_all(N-2)):
        c='1' + e + '1'
        success, t=test_str(c)
        if success:
            res.append([c, t])
        if len(res) >= J:
            return res 
    return res


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i:" % (1+i_test)
        tmp=[e[0] for e in res]
        if not len(tmp) == len(set(tmp)):
            raise
        for c, l in res:
            print str(c) + ' ' + ' '.join([str(e) for e in l])

def check(filename):
    with open(filename) as f:
        csv_r=csv.reader(f, delimiter=' ')
        csv_r.next()
        t=0
        for row in csv_r:
            t+=1
            n=row[0]
            for i in xrange(1,len(row)):
                if int(n, i+1) % int(row[i]) != 0 or int(n, i+1)==int(row[i]):
                    raise
        print 'total', t



if __name__ == '__main__':
    #main('./B-large.in')
    #main('./simple.in')
    #main('./B-small-attempt1.in')
    #main('./C-small-attempt0.in')
    #check('./simple.out')
    check('./C-small-attempt0.out')
    #prime_lst=primesfrom2to(10**9)
    #print prime_lst
    #print test_str('1001')
    #print test_str('100011')

