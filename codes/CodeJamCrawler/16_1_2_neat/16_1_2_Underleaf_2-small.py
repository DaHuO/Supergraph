# -*- coding: utf-8 -*-
import fractions
import math


#file = open('Inputs/Input.in', 'r')
with open('Inputs/B-large.in', 'r') as infile, open('Outputs/Output.out', 'w') as outfile: 
   
    T = int(infile.readline().split('\n')[0]);
    
    for i in range(0,T):
        
        N = int(infile.readline().split('\n')[0]);
        listInts = [0] * 2500 
        for j in range(0,(2*N-1)):
        
            listaStr = infile.readline().split('\n')[0].split(' ');
            for c in listaStr:
                listInts[int(c)-1] += 1
       
        S = [x for x in range(0,2500)]
        M = [x+1 for x in S if listInts[x] % 2 == 1]
        result = reduce( (lambda x, y: x + y), [str(x)+' ' for x in sorted(M)])

        print 'Case #'+str(i+1)+': '+str(result)
        outfile.write('Case #'+str(i+1)+': '+str(result)+'\n')      
        
        


        
    
    
    
