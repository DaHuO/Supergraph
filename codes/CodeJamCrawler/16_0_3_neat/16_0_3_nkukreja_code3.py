#!/usr/bin/python
import itertools 
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True  

def ntobase(n,b):
    i=0
    sum = 0
    for i in range(0,len(n)):
        sum+=n[len(n)-1-i] * pow(b,i)
    return sum

def ntdiv(n):
    i=2
    while (i< n):
        if (int(n) % i) == 0:
            return i
        i=i+1

def solve(I,n,m):
    lst = map(list, itertools.product([0, 1], repeat=n))
    print ("Case #%s:" % I)
    run = 0
    for i in lst:
        if i[0] == 1 and i[n-1] == 1:
            s = "".join(str(x) for x in i)
            cnt = 0
            b = []
            for base in range(2,11):
                if (is_prime(ntobase(i,base))):
                    break
                else:
                    cnt = cnt+1
                    b.append(ntdiv(ntobase(i,base)))

            if cnt == 9:
                print s," ".join(str(x) for x in b)
                run = run+1
                if run == m:
                    return

    return

t = int(input())
for i in range(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    solve(i,n,m)