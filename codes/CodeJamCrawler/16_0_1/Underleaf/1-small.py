# -*- coding: utf-8 -*-
import fractions
import math

def parseString(cost,stringRest,stringAtual):

   if len(stringRest) == 0:
       return [cost,stringAtual];
   else :
       char = stringRest[0];
       direita = stringAtual[-1];
       esquerda = stringAtual[0];
       if(char > direita):
           result1 = parseString(cost+1,stringRest[1:],char+stringAtual)
       else :
           result1 = parseString(cost,stringRest[1:],char+stringAtual)
       if(char < esquerda):
           result2 = parseString(cost+1,stringRest[1:],stringAtual+char)
       else:
           result2 = parseString(cost,stringRest[1:],stringAtual+char)
   if result1[0] > result2[0]:
       return result1
   else :
       return result2


#file = open('Inputs/Input.in', 'r')
with open('Inputs/A-small-attempt0.in', 'r') as infile, open('Outputs/Output.out', 'w') as outfile: 
   
    T = int(infile.readline().split('\n')[0]);
    
    for i in range(0,T):
        
        listaStr = infile.readline().split('\n')[0]
        result = parseString(0,listaStr[1:],listaStr[0])[1];
       

        print 'Case #'+str(i+1)+': '+str(result)
        outfile.write('Case #'+str(i+1)+': '+str(result)+'\n')      
        
        


        
    
    
    
