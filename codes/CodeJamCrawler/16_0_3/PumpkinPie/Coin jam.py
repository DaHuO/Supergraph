from __future__ import division

import os
import os.path, time
import itertools
from random import randint

def isprime(n):
    if n == 2:
        return 0
    if n == 3:
        return 0
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return 0


def isdiv(n,num):
    if n % num == 0:
        return num
    return 0

def basegen(x):
        Arr=[]
        Div=[]
        for i in range(2,11):
                '''if isprime(int(x,i))==0:
                        break
                else:
                        Arr.append(int(x,i))
                        Div.append(isprime(int(x,i)))'''
                if isdiv(int(x,i),i+1)==0:
                        break
                else:
                        Arr.append(int(x,i))
                        Div.append(isdiv(int(x,i),i+1))
        if len(Arr)==9:
                return Div
        else:
                return "No"
                
        
        
        
                
        
        


fo=open("test.txt")
fw=open("test_out.txt","w")
#fo=open("A-small-attempt0.in")
#fw=open("A-small-attempt0.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline().split()
        Length=int(Line[0])
        Number=int(Line[1])
        gentot=0
        print "Case #"+ str(k+1)+": "
        fw.write("Case #"+ str(k+1)+": \n")
        i=1
        Addarray=[]
        for i in range(10):
                Addarray.append(i*10**Length+i)
        print Addarray    
        while gentot<Number:
                middle=str("{0:b}".format(i)).zfill(Length-2)
                string="1"+middle+"1"
                answer=basegen(string)
                if answer!="No":
                        fw.write(str(string)+" "+str(" ".join(str(x) for x in answer))+"\n")
                        gentot=gentot+1
                        print str(string)+" "+str(" ".join(str(x) for x in answer))+"\n"
              
                i=i+1
                print gentot
                
    
     
fw.close()        
        
                





