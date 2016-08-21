import math
import numpy as np
import sys
from sets import Set

f=open('A-large.in', 'r')
f2=open('Counting_sheep_large.ou', 'w')
init=0
case=1
for line in f:
    #print(line)
    if init==0:
        total=line
        init=1
    else:
        aux=line.strip()
        aux=int(aux)
        sit=Set()
        [sit.add(i) for i in str(aux)]
        #print(sit)
        count=2
        aux_i=aux
        while(len(sit) < 10 and aux !=0):
            aux=count*aux_i
            [sit.add(i) for i in str(aux)]
            count=count+1
            
        f2.write('Case #')
        f2.write(str(case))
        f2.write(': ')
        if aux!=0:
            f2.write(str(aux))
        else:
            f2.write('INSOMNIA')
        f2.write('\n')
        sys.stdout.write('Case #')
        sys.stdout.write(str(case))
        sys.stdout.write(': ')
        if aux!=0:
            sys.stdout.write(str(aux))
        else:
            sys.stdout.write('INSOMNIA')
        sys.stdout.write('\n')
        case=case+1