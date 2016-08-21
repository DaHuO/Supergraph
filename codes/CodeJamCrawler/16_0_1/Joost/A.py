#! /usr/bin/env python

fname = 'A-large'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')


def solve(fin):
    x = int(fin.readline())
    if x == 0:
        return "INSOMNIA"
    a = 0
    n = x
    while True:
        m = n
        while m > 0:
            a |= (1 << (m % 10))
            m //= 10
        if a == 1023:
            return n
        n += x

T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
