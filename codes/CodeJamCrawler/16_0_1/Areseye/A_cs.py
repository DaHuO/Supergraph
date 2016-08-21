#encoding:utf-8

import os
import sys


def looptest():
    for i in range(1000,8000):
        print 'i=',i
        print 'min number:',solve_brute(i)


def collectdigits(num,visset):
    while num>0:
        digit = num%10
        if digit not in visset:
            visset.add(digit)
        num /= 10
def solve_brute(val):
    if val == 0:
        return 0
    visnum = set()
    for i in range(1,10000):
        num = val*i
        collectdigits(num,visnum)
        if len(visnum)==10:
            # print 'num:',num
            return num
        
def small_input():
    resarr = []
    with open('a.in','r') as fin:
        for ind,line in enumerate(fin):
            if ind==0:
                T = int(line)
            else:
                res = solve_brute(int(line))
                resarr.append(res)
                

    with open('a.out','w') as fout:
        for ind,res in enumerate(resarr):
            if res is 0:
                fout.write('Case #{}: INSOMNIA\n'.format(ind+1))
            else:
                fout.write('Case #{}: {}\n'.format(ind+1,res))

    

if __name__ == '__main__':
    small_input()
    # looptest()
