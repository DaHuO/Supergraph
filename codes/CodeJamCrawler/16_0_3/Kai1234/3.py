import itertools
import signal, os
def bitGen(n):
    for i in itertools.product('01', repeat=n):
        yield ''.join(i)

"""
def bitGen(n):
    return [''.join(i) for i in itertools.product('01', repeat=n)]
"""

import math

input()
input()
n=30
count=0

def get_first_divisor(num):
    for i in range(2,num):
        if(num%i)==0:
            return i

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]



def runFunctionCatchExceptions(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception:
        return ["exception", "boohoo"]

    return ["RESULT", result]


def runFunctionWithTimeout(func, args=(), kwargs={}, timeout_duration=10, default=None):
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default
        def run(self):
            self.result = runFunctionCatchExceptions(func, *args, **kwargs)
    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return default

    if it.result[0] == "exception":
        return 0;

    return it.result[1]


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def dothings(i):
    l=False
    for j in range(2,11):
        num=int(i,j)
        boole=is_prime(num)
        if(boole):
           l=True
           break
    return l

def printhings(i):
    daddydivList=[]
    s=""
    for j in range(2,11):
        num=int(i,j)
        divList=get_first_divisor(num)
        daddydivList.append(divList)
    s+=str(i)+" "
    for num in daddydivList:
        s+=str(num)+" "
    return s

count=0
for i in (bitGen(n)):
    i="1"+i+"1"
    if(count>=500):
        break
    divs=[]
    """
    """
    #print(i)
    try:
        l=(runFunctionWithTimeout(dothings,(i,),timeout_duration=0.02))
        #print(l)
    except(Exception) as e:
        #print(e)
        l=True
        continue
    if(not l):
        try:
            s=runFunctionWithTimeout(printhings,(i,),timeout_duration=0.02)
            if(s):
                print(s)
        except:
            #print(e)
            continue


