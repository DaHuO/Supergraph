# -*- coding: utf-8 -*-
a=open("C:\\GoogleCodeJam\\panCakes\\\\B-large.IN",'r')
b=a.read()
lines=b.split("\n")

tests=[]


def flip(chaine,i):
    r=''
    for j in range(i,-1,-1):
        if chaine[j]=='+' :       
            r+='-'
        else:
            r+='+'
    r+=chaine[i+1:]    
    return r 
    
def trouveDernierMoinsEnPartantFin(chaine):
    l=len(chaine)
    for i in range(l-1,-1,-1):
        if chaine[i]=='-':
            return i
    return -1  

def trouveNombrePlusFin(chaine):
    l=len(chaine)
    c=0
    for i in range(l-1,-1,-1):
        if chaine[i]=='-':
            return c
        c+=1 
    return c 

def trouveNombreMoinsFin(chaine):
    l=len(chaine)
    c=0
    for i in range(l-1,-1,-1):
        if chaine[i]=='+':
            return c
        c+=1 
    return c     
  
    
    
def trouveNombrePlusDebut(chaine):
    for i in range(len(chaine)):
        if chaine[i]=='-':
            return i
def trouveNombreMoinsDebut(chaine):
    for i in range(len(chaine)):
        if chaine[i]=='+':
            return i
            

          
def transforme(chaine,tour):
    print(chaine)
    print('tour '+str(tour))
    l=len(chaine)
    pf=trouveNombrePlusFin(chaine)
    if len(chaine)-pf==0:
        t=tour
        print("trouvé")
        return t
        
    else:
        chaineTp=chaine[:l-pf]
        #mf=trouveNombreMoinsFin(chaineTp)
        if chaineTp[0]=='-':
            return transforme(flip(chaine,len(chaineTp)-1),tour+1)
        else:
            pd=trouveNombrePlusDebut(chaineTp)
            return transforme(flip(chaine,pd-1),tour+1)
                 
    
  

class Test:
    def __init__(self,line):
        self.line=line
        
    def traite(self):
        return str(transforme(self.line,0))
        
            

N=int(lines[0])
i=1
for a0 in range(N):
   line=lines[i]
   tests.append(Test(line))
   i+=1
        
a.close()    


                            


c=open("C:\\GoogleCodeJam\\panCakes\\output.txt",'w')    

for i in range(len(tests)):
    c.write("Case #"+str(i+1)+": "+(tests[i].traite()+"\n")) 
    print("Case #"+str(i+1)+": "+(tests[i].traite()+"\n"))  
c.close()                         