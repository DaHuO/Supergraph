# -*- coding: utf-8 -*-
a=open("C:\\GoogleCodeJam\\digits\\A-small-attempt0.txt",'r')
b=a.read()
lines=b.split("\n")

tests=[]

dig=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']


def retireLettre(s,a):
    if s is None:
        return None
    if a in s:
        index=s.find(a)
        s1=s[:index]+s[index+1:]
        return s1

def retireMot(s,mot):
    if s is None:
        return ''
    s1=s
    for lettre in mot:
        s1=retireLettre(s1,lettre)
    return s1



def motPresent(s,mot):
    if s is None:
        return False
    for e in mot:
        if e not in s:
            return False
    return True
    

                
def teste(s,dig):
    li=[]
    temp=[]
    for e in dig:
        if motPresent(s,e):
            temp.append([e,retireMot(s,e)])
    while len(temp)>0:        
        for el in temp:
            if el[-1]=='':
                return el
            else:
                for e in dig:
                    if motPresent(el[-1],e):
                        res=el[:-1]
                        res.append(e)
                        res.append(retireMot(el[-1],e))
                        li.append(res)
        temp=li
        li=[]
    
def rendRes2(s,dig):
    liste=[]
    
    for e in teste(s,dig):
        if e in dig:
            liste.append(dig.index(e))
    liste=sorted(liste)
    res=''
    for e in liste:
        res+=str(e)
    return res        


class Test:
    def __init__(self,s):
        self.s=s

        
    def traite(self,dig):
        return rendRes2(self.s,dig)
        
            

N=int(lines[0])
i=1
for a0 in range(N):
   s=lines[i]

   tests.append(Test(s))
   i+=1
        
a.close()    


                            


c=open("C:\\GoogleCodeJam\\digits\\output.txt",'w')    

for i in range(len(tests)):
    c.write("Case #"+str(i+1)+": "+(tests[i].traite(dig)+"\n"))
    print(tests[i].s)
    print("Case #"+str(i+1)+": "+(tests[i].traite(dig)+"\n"))

c.close()                         