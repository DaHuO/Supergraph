from itertools import *
from math import *
from functools import *
from collections import Counter
import sys
letters = list(map(Counter,("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")))

def f(s):
    nbofchars = Counter(s)
    d = ['Z', 'O', 'W', 'R', 'U', 'F', 'X', 'S', 'G', 'I']
    res = []
    for i  in [0,2,4,6,8,1,3,5,7,9]:
        m = nbofchars[d[i]]
        # print(nbofchars)
        # print(m, d[i], i)
        if  m > 0:
            for key, value in (letters[i].items()):
                nbofchars[key] -= m*value
            res.extend([i]*m)
        # print(nbofchars)
            
    if any(nbofchars.values()):
        raise ValueError(s)
    return ''.join(map(str,sorted(res)))


t = int(input())
for i in range(1, t+1):
    s = input()

    print("Case #%d: %s " % (i, f(s)))
