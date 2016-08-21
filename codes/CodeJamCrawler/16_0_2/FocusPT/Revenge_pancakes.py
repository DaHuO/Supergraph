import math
import numpy as np
import sys
from sets import Set


f=open('B-large.in', 'r')
f2=open('revenge_pancakes_large.ou', 'w')
init=0
case=1
for line in f:
    #print(line)
    if init==0:
        total=line
        init=1
    else:
        aux=list(line.strip())
        test=['+']*len(aux)
        flipin=len(aux)-1
        result=0
        while cmp(aux,test)!=0:
            if aux[flipin]=='-':
                if aux[0]=='-':
                    aux2=[]
                    for i in aux[0:flipin+1]:
                        if i == '+':
                            aux2.append('-')
                        else:
                            aux2.append('+')
                    aux[0:flipin+1]=list(reversed(aux2))
                    result=result+1
                  
                else:
                    aux3='+'
                    count=-1
                    while aux3=='+':
                        count=count+1
                        aux3=aux[count]
                    ##print(count)
                    aux2=[]
                    for i in aux[0:count]:
                        if i == '+':
                            aux2.append('-')
                        else:
                            aux2.append('-')
                    aux[0:count]=list(reversed(aux2))
                    result=result+1
                #print(aux)
            else:
                flipin=flipin-1
            
        
        f2.write('Case #')
        f2.write(str(case))
        f2.write(': ')
        f2.write(str(result))
        f2.write('\n')
        sys.stdout.write('Case #')
        sys.stdout.write(str(case))
        sys.stdout.write(': ')
        sys.stdout.write(str(result))
        sys.stdout.write('\n')
        case=case+1        