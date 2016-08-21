# Hello World program in Python

import math
from itertools import count,islice
    
ini=2**15 + 1
bin=[]
count=0
print "Case #1: "
while ini<2**16 and count<50:
    bin=list('{0:0b}'.format(ini))
    #lislen=len(bin)
    num=2
    arr=[]
    string_bin=''
    #k=1
    while num<11:
        initial_num=0;
        i=0
        '''for i in range(0,lislen):
            if bin[i]=='1':
                initial_num+=num**(i)'''
        string_bin=''.join(bin)
        initial_num=int(string_bin,num)
        
        #print initial_num
        
        sqt=int(round(math.sqrt(initial_num)))
        '''if initial_num%2==0:
            arr.append(i)
        else:'''
           
        for i in xrange(2,sqt+1): 
            if initial_num%i==0:
                arr.append(str(i))
               # print num
                break
        #print i
        if i>=sqt: 
            arr=[]
            num=2
            break
        
        num+=1
    
	
    if num==11:
        count+=1
        print string_bin,' '.join(arr)
    ini+=2
