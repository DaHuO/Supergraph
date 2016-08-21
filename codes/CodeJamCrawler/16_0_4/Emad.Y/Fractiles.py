# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:13:05 2016

@author: Emad Yehya
"""

#only works for easy

i = open('D-small-attempt0.in', 'r')
o = open('out.txt', 'w')

T = int(i.readline())

for t in range(1, T+1):
    l = i.readline().split(' ')
    K = int(l[0])
    C = int(l[1])
    S = ""
    for x in range(0, K):
        S += str(1+x*K**(C-1)) + " "
    o.write("Case #" + str(t) + ": " + S + "\n")
    