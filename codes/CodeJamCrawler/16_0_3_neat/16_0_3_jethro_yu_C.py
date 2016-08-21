#!/usr/bin/python
import itertools
import multiprocessing
import sys
import pyprimes

from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
        pass
class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

raw_input()
[N, J] = map(int, raw_input().split())
print "Case #1:"

def base(s,b):
    if(b==10):
        return int(s)
    sum = 0
    factor = 1
    for i in s[::-1]:
        sum += factor*int(i)
        factor *= b
    return sum

def worker(s ,queue):
    ans = s
    for b in range(2, 11):
        num = base(s, b)
        factor = 0
        if pyprimes.fermat(num):
            ans = 0
            break
        with timeout(seconds=1):
            try:
                factor = pyprimes.factorise(num).next()[0]
            except:
                ans = 0
                break
        if factor == num:
            ans = 0
            break
        ans = ans +" "+ str(factor)
        #factors = pyprimes.factors(num)
        #if len(factors) == 1:
        #    ans = 0
        #    break
        #ans = ans +" "+ str(factors[0])

    queue.put(ans)

pool = multiprocessing.Pool(processes=32)
m = multiprocessing.Manager()
q = m.Queue()
working = 0
count = 0
max_num = 2**(N-2)
i = itertools.count()

for i in itertools.count():
    if(working <32 and i < max_num):
        s=("1{0:>0"+str(N-2)+"b}1").format(i)
        pool.apply_async(worker, (s, q))
        working +=1
        continue
    ans = q.get()
    working -=1
    if ans == 0:
        continue
    count += 1
    print ans
    if count == J:
        sys.exit()
