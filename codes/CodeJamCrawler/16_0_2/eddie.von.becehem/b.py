from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

T = int(stdin.readline())

def flip(x):
    if x == '+':
        return '-'

    return '+'

dic = {}

def fliplong(s):
    if s in dic:
        return dic[s]

    l = len(s)

    news = ""
    
    for i in range(l):
        news += flip(s[l - i - 1])

    dic[s] = news
    return news

def sol(lis):

#    print "benoit", len(lis), [x for (x, y) in lis]
    #print "benoit", len(lis), len([x for (x, y) in lis]), alreadyviewed

    # take the first
    arr, x = lis[0]

    # Won
    if '-' not in arr:
        return x

    # Try all possibilities
    for n in range(1,len(arr)+1):
        newarr = fliplong(arr[0:n]) + arr[n:]
#        print "->", newarr
        if newarr not in alreadyviewed:
            lis.append((newarr, x + 1))
            alreadyviewed.append(newarr)

    return sol(lis[1:])

for i in range(1,T+1):

    arr = stdin.readline().rstrip()
    alreadyviewed = []

    print "Case #" + str(i) + ":", 
    print sol([(arr, 0)])



