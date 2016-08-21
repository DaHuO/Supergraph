# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:23:59 2016

@author: Emad Yehya
"""

i = open('A-large.in', 'r')
o = open('out.txt', 'w')

T = int(i.readline())

for t in range(1, T+1):
    n = int(i.readline())
    if(n == 0):
        o.write("Case #" + str(t) + ": INSOMNIA\n")
        continue
    D = [False]*10
    orn = n
    rem = 10
    M = 0
    while(rem > 0):
        n2 = n
        while(n2 > 0):
            if(D[n2%10] == False):
                D[n2%10] = True
                rem-=1
            n2 /= 10
        n += orn
        M += 1
    o.write("Case #" + str(t) + ": " + str(n-orn) + "\n")