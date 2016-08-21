from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

dic = {}

def dig(n):

    if n == 0:
        return [0]

    ans = set([])

    while n > 0:
        ans.add(n % 10)
        n = n / 10

    return ans

def sol(n):

    if n == 0:
        return 'INSOMNIA'

    mn = n

    if n in dic:
        return dic(n)
       
    allans = dig(n)

    while len(allans) != 10:
        mn += n
        for x in dig(mn):
            allans.add(x)

    return mn

T = int(stdin.readline())

for i in range(1,T+1):

    n, = map(int, stdin.readline().split())
    
    print "Case #" + str(i) + ":", 
    print sol(n)
    
