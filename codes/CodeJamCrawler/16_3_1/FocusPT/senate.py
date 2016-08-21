import math
import numpy as np
import sys
from sets import Set
import copy



f=open('senate_large.in', 'r')
f2=open('senate_large.ou', 'w')
init=0
case=1
T=f.readline()
solution = []
aux3=[]
while case <= int(T):
    solution = []
    N=f.readline()
    b=f.readline()
    list=b.split()
    list=map(int,list)
    
    while sum(list)!=0: 
        m=max(list)
    
        aux=[i for i, j in enumerate(list) if j == m]
        t_list=copy.deepcopy(list)
        flag=0
        #print(list)
        t_list[aux[0]]= int(t_list[aux[0]])-1
        #print m
        #print list
        if sum(list)>2 and m>1:    
            for aux2 in range(0, len(list)):
                k=0
                if aux2 == aux[0]:
                    k=2
                if (float(list[aux2])-k)/(sum(list)-2)>0.5:
                    flag=1
        else:
            flag=1
            
        if flag==1:
            
            m=max(t_list)
            aux3=[i for i, j in enumerate(t_list) if j == m]
            if sum(list)>=2 and m>0:
                if m>0 and sum(map(int,list))>2:
                    for aux2 in range(0, len(list)):
                        k=0
                        if aux2== aux3[0] or aux2 == aux[0]:
                            k=1
                        if (float(list[aux2])-k)/(sum(map(int,list))-2)>0.5:
                                flag=2
            else:
                flag=2
        
        if flag==0:
            list[aux[0]]=int(list[aux[0]])-2
            solution.append(chr(65+aux[0]))
            solution.append(chr(65+aux[0]))
            solution.append(" ")
        if flag==1:
            list[aux[0]]=int(list[aux[0]])-1
            list[aux3[0]]=int(list[aux3[0]])-1
            solution.append(chr(65+aux[0]))
            solution.append(chr(65+aux3[0]))
            solution.append(" ")
        if flag==2:
            list[aux[0]]=int(list[aux[0]])-1
            solution.append(chr(65+aux[0]))
            solution.append(" ")
            
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
        