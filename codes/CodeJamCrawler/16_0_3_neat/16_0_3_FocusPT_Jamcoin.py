import math
import numpy as np
import sys
from sets import Set
import time

def is_prime(a,b):
    count=0
    if a%2==0:
        return [0,2]
    if a%3==0:
        return [0,3]
    
    root=int(math.floor(math.sqrt(a)))
    i=5
    while i<=root and count<1000:
        if a%i==0:
            return [0,i]
        if a%(i+2)==0: 
            return [0,i+2]
        i=i+6
        #print(i)
        count=count+1
    #for i in range(3, int(math.floor(math.sqrt(a))),2):
        #if i%b!=0:
    #    if a%i ==0:
    #        return [0,i]
        
    #print ("a")
    return [1,0]
    
    
    #return all(a%i for i in range(2, a))


#def numiber(a):
#    ai= [a%i for i in xrange(2, a)]
#    return 2+ ai.index(0)

f=open('C-large.in', 'r')
f2=open('jamcoin_big.ou', 'w')
init=0
case=1
aaaaaai=0
for line in f:
    #print(line)
    if init==0:
        total=line
        init=1
    else:
        aux=line.strip()
        aux=aux.split()
        N=int(aux[0])
        J=int(aux[1])
        answers=0
        mini=2**(N-1)+1
        f2.write('Case #')
        f2.write(str(case))
        f2.write(':\n')
        sys.stdout.write('Case #')
        sys.stdout.write(str(case))
        sys.stdout.write(':\n')
        start_time = time.time()
        while answers<J:     
            #print mini
            a="{0:b}".format(mini)
            bases=[]
            negate=0
            #a='100011'
            
            #print mini
            if a[-1]=='1' and a[0]=='1':
                
                save=[]
                for i in range(2,11):
                    #aa=sum([int(a2)*(i**b2) for a2,b2 in zip(a,range(len(a)-1,-1,-1))])
                    aa=int(a,i)
                    #print(aa)
                    #save.append(aa)
                    aaaaaa=time.time()
                    aiii=is_prime(aa,i)
                    aaaaaai=aaaaaai+time.time()-aaaaaa
                    if(aiii[0]==1):
                        negate=1
                        break
                    save.append(aiii[1])
                if negate==0:
                    answers=answers+1
                    
                    f2.write(a)
                    sys.stdout.write(str(answers))
                    sys.stdout.write('    ')
                    
                    sys.stdout.write(str(a))
                    #print(save)
                    #a=[numiber(i) for i in save]
                    for i in save:
                        f2.write(' ')
                        sys.stdout.write(' ')
                        f2.write(str(i))
                        sys.stdout.write(str(i))
                    f2.write('\n')
                    sys.stdout.write('\n')
                    mini=mini+1
                else:
                    mini=mini+1
            else:
                    mini=mini+1
            
        print(time.time()-start_time)    
        print(aaaaaai)   