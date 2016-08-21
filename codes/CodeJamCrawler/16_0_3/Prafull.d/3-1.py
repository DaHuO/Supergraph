from math import *
def fun(n):
    s=int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            break
    if i==s:
        return -1
    else:
        return i
n,j=map(int,raw_input().split())
print "Case #1:"
s="1"+"0"*(n-2)+"1"
v=int(s,2)
case=1
while case<=j:
    b=str(bin(v))[2:]
    a=[0]*9
    for i in range(2,11):
        no=int(b,i)
        k=fun(no)
        if k==-1:
            break
        else:
            a[i-2]=k
    if k!=-1:
        print b,
        for i in a:
            print i,
        print
        case=case+1
    v=v+2
    
    
