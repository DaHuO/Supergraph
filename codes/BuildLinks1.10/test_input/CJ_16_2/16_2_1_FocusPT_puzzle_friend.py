import math
import numpy as np
import sys
from sets import Set
import copy

f=open('puzze_l.in', 'r')
f2=open('puzzle.ou', 'w')
init=0
case=1
numbers=['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
for line in f:
    #print(line)
    if init==0:
        total=line
        init=1
    else:
        aux=line.strip()
        ai=copy.deepcopy(aux)
        
        ai=list(ai)
        flag=0
        solution=[]
        while 'Z' in ai:
            solution.append(0)
            for a in numbers[0]:
                ai.remove(a)
        
        while 'W' in ai:
            solution.append(2)
            for a in numbers[2]:
                ai.remove(a)
        
        while 'U' in ai:
            solution.append(4)
            for a in numbers[4]:
                ai.remove(a)
        
        while 'X' in ai:
            solution.append(6)
            for a in numbers[6]:
                ai.remove(a)
        
        while 'O' in ai:
            solution.append(1)
            for a in numbers[1]:
                ai.remove(a)
        
        
        
        while 'F' in ai:
            solution.append(5)
            for a in numbers[5]:
                ai.remove(a)
        
        while 'G' in ai:
            solution.append(8)
            for a in numbers[8]:
                ai.remove(a)
        while 'T' in ai:
            solution.append(3)
            for a in numbers[3]:
                ai.remove(a)
        while 'S' in ai:
            solution.append(7)
            for a in numbers[7]:
                ai.remove(a)
        while 'N' in ai:
            solution.append(9)
            for a in numbers[9]:
                ai.remove(a)               
        solution.sort()
        
        f2.write('Case #')       
        f2.write(str(case))
        f2.write(': ')
        for z in solution:
            f2.write(str(z))
        f2.write('\n')
        sys.stdout.write('Case #')
        sys.stdout.write(str(case))
        sys.stdout.write(': ')
        for z in solution:
            sys.stdout.write(str(z))
        sys.stdout.write('\n')
        case=case+1