# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:13:11 2016

@author: huisu
"""

def solution(n):
    numset = set([])
    if n == 0:
        return 'INSOMNIA'
    count = 1
    while len(numset)!=10:
        strn = str(n*count)
        for i in strn:
            if i not in numset:
                numset.add(i)        
        count += 1
    return strn

if __name__ == '__main__':
    fp = open('A-large.in')
    n = fp.readline()
    f = open("output", 'w+') 
    for i in range(int(n)):
        line = fp.readline()
        f.write("Case #"+str(i+1)+": "+str(solution(int(line)))+'\n')
    fp.close()
    f.close()
         
   
        