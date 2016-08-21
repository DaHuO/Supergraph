# -*- coding: utf-8 -*-
"""
Google Jam
Qualification Round - Task 1
Created on Fri Apr 10 21:22:52 2015

@author: petrs
"""

def digits(x):
    str(x).split()

def sheep(x):
    if x == 0:
        return "INSOMNIA"
    digits = set(list(str(x)))
    final = x    
    while len(list(digits)) < 10:
        final += x
        digits = digits | set(list(str(final)))
    return final    

f = open('C:\Users\petrs\Downloads\A-small-attempt1.in', 'r')

N = int(f.readline().split()[0])

answers = list()
for i in range(201):
    x = sheep(i)
    answers.append(x)

for i in range(N):
    a = int(f.readline().split()[0])

    if a==0:
        print "Case #%i: INSOMNIA" % i
    else:
        print "Case #%i: %i" % (i+1,answers[a])
f.close()