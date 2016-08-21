# -*- coding: utf-8 -*-

from random import randint
import math

def solve(n, j):
    jamcoins = []
    while len(jamcoins) < j:
        # random jamcoin
        jc = "1"+"".join([str(randint(0,1)) for _ in range(n-2)])+"1"
        divisors = []
        for b in range(2,11):
            jc_nb = int(jc,b)
            div_found = False
            for d in range(3,int(math.sqrt(jc_nb))+1,2):
                if jc_nb % d == 0:
                    divisors.append(d)
                    div_found = True
                    break
            if not div_found:
                break
        if len(divisors) == 9: # 2 to 10
            jamcoins.append(jc + " " + " ".join([str(d) for d in divisors]))
    return "\n".join(jamcoins)


t = int(input())
for i in range(t):
    n, j = input().split()
    print("Case #" + str(i+1) + ":\n" + solve(int(n),int(j)))
