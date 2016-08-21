#!/usr/bin/python

import sys


def chk(a):
    for i in range(0, 10):
        if (a[i] == 0):
            return 0
    return 1


def fun(N):
    while(N>0):
        p=N%10
        a[p] = 1
        N=N/10 

f = open('A-large.in.txt', 'r')
t= int(f.readline())

# t= int(raw_input())

k= open('op.txt', 'w')
sys.stdout = k

for i in range(0,t):
    
    a=[0,0,0,0,0,0,0,0,0,0]

    k = 1

    n = N = int(f.readline())
    # n = N = int(raw_input())
    print "Case #" + str(i+1) + ":",

    while(1):
        fun(N)
        if (chk(a) == 0):
            k += 1
            N=n*k
            if (N==n):
                print "INSOMNIA"
                break
        else:
            print n*k
            break
f.close()            
                