# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:19:47 2016

@author: mattia

Google Code Jam 2016 Q1

Dato un numero N, contare N, 2N, 3N, ... , finché nei vari numeri non sono
state viste tutte le cifre da 0 a 9 almeno una volta.
Stampare l'ultimo numero nominato.
"""

def find_digits(N):
    """returns the digits of N. N is a string"""
    digs = []
    for ch in N:
        digs.append(int(ch))
    return digs
    
def complete(vec):
    return sum(seen_digits) == len(seen_digits)

with open('A-large.in','r') as f, open('out.txt', 'w') as fout:
    n_cases = int(f.readline())
    for case in range(1, n_cases+1):
        N = f.readline()
        stop = False
        seen_digits = [False] * 10
        if int(N) == 0:
            tmp = 0
            stop = True

        i = 1
        while not stop:
            tmp = str(i*int(N))
            digs = find_digits(tmp)
            for n in digs:
                seen_digits[n] = True
            if complete(seen_digits):
                stop = True
            i += 1
        if tmp == 0:
            fout.write('Case #' + str(case) + ": INSOMNIA\n")
        else:
            fout.write('Case #' + str(case) + ": " + str(tmp) + '\n')