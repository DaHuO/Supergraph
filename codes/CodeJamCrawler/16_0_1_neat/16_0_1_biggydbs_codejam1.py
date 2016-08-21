from math import factorial as fff
from fractions import gcd 
f=pow(2,3,3)
xs=fff(f+2)
author='biggy_bs'
# Main code goes here !!
t=input()
case=1
while t>0:
    t-=1
    n=input()
    if n==0:
        print 'Case #'+str(case)+': '+'INSOMNIA'
    else:
        flag=0
        ct=1
        dic={}
        while 1:
            flag=0
            s=ct*n
            s=str(s)
            for i in s:
                try:
                    dic[i]+=1
                except:
                    dic[i]=1
            for i in range(10):
                try:
                    q=dic[str(i)]
                except:
                    flag=1
            if flag==0:
                break
            ct+=1
        print 'Case #'+str(case)+': '+str(ct*n)
    case+=1
