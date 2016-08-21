# -*- coding: utf-8 -*-
a=open("C:\\GoogleCodeJam\\CountingSheep\\\\A-large.in",'r')
b=a.read()
lines=b.split("\n")

tests=[]

class Test:
    def __init__(self,C):
        self.C=C
        
    def traite(self):
        print(self.C)
        records=[]
        for e in str(self.C):
            if e not in records:
                records.append(e)
        if len(records)==10:
            return self.C
        i=2
        N=self.C
        rounds=0
        while len(records)<10 and rounds<100:
            print(N)
            N=i*self.C
            for e in str(N):
                if e not in records:
                    records.append(e)  
            print(records)        
            rounds+=1 
            i+=1 
            if len(records)==10:
                return str(N)
        
        return "INSOMNIA"   
   
            

N=int(lines[0])
i=1
for a0 in range(N):
   C=int(lines[i])
   tests.append(Test(C))
   i+=1
        
a.close()    


                            


c=open("C:\\GoogleCodeJam\\CountingSheep\\output.txt",'w')    

for i in range(len(tests)):
    c.write("Case #"+str(i+1)+": "+(tests[i].traite()+"\n")) 
    print("Case #"+str(i+1)+": "+(tests[i].traite()+"\n"))  
c.close()              
print(tests[1].traite())           