#! /usr/bin/env python

import signal
class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

def isprime(n):
    if n < 2:
        return False
    elif n%2==0 and n>2:
        return False
    else:
        return all(n%i for i in xrange(3,int(n**0.5)+1,2))

def factor(n):
    from itertools import count
    #for i in xrange(2,int(n**0.5)+1):
    for i in iter(count(2).next, n): # Dont want extra things, since only 1 factor needed.
        if n%i == 0:
            return i

def stuff(i, bases):
    a = []
    if not any(isprime(int(i, base)) for base in bases):
        #print all(isprime(int(i,base)) for base in bases)
        a.append(i)
        for base in bases:
            a.append(factor(int(i,base)))
        a = map(str,a)
        a = " ".join(a)
        return a


    
t = int(raw_input())
N,J = map(int, raw_input().split())
smallest = '0'*(N-2)
largest = '1'*(N-2)
smallest = int(smallest,2)
largest = int(largest,2)
numbers = ('1'+ bin(x)[2:].zfill(N-2)+'1' for x in xrange(smallest,largest+1))

bases = range(2,11)
count1 = 1
print "Case #1: "
while count1<=J: 
    i = next(numbers)    
    signal.setitimer(0,0.05)
    try:
        a = stuff(i,bases)
        if a:
            print a
            count1 +=1
    except TimeoutException:            
        continue
    else:
        signal.alarm(0)
        
        
