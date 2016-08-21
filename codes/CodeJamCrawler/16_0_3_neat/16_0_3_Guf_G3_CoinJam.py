# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:28:50 2016

@author: zozo
"""


import math

fname = 'C-small-attempt0.in'
f = open(fname,'r')

nlines = f.readline().replace('\n','') #
inputs = []
for l in range(int(nlines)):
    inputs.append(f.readline().replace('\n',''))

f.close()


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

foutput=''
ii = 0
for inp in inputs:
    ii+=1
    lst = inp.split(' ')
    N = int(lst[0])
    J = int(lst[1])
    foutput +='Case #' + str(ii) + ':\n'    
    
    j = 1
    for i in range(2**(N-2)):
        num= '1' + str(bin(i)).replace('0b','').zfill(N-2) + '1'
        outputstr = num + ' ' 
        for k in range(2,11):
            res = is_prime(int(num,k))
            if res == 0: 
                outputstr = ''            
                break
            else:
                outputstr += str(res) + ' '
            
        if outputstr != '':
            foutput += outputstr[:len(outputstr)-1]+'\n'
            j+=1
            
        if j>J:
            break





  
fout = open('fout','w')     
fout.write(foutput)
    
fout.close()