from math import *
lp=[0]*9000001
pr=[]
def er():
    n=9000000
    for i in range(2,n+1):
        if lp[i]==0:
            lp[i]=1
            pr.append(i)
        j = 0
        while j < len(pr) and pr[j]<=lp[i] and i*pr[j]<=n:
            print(j)
            lp[i*pr[j]]=pr[j]
            j+=1

def bin1(s):
    s = s[1:-1]
    k = int(s,2)
    k+=1
    b = str(bin(k))[2:]
    return '1'+'0'*(len(s)-len(b))+b+'1'

def f(s):
    de = []
    for i in range(2,11):
        d = int(s,i)
        fl = False
        for j in pr:
            if sqrt(d)<j:
                break
            if d%j == 0:
                de.append(j)
                fl = True
                break
        if not fl:
            return [False,de]
    return [True,de]

er()
t = input()
[n,j]=[int(x) for x in input().split(' ')]
start = ['0']*n
start[0]='1'
start[-1]='1'
s = ''.join(start)
k = int(s, 2)
fin = int('1'*n,2)
i = 0
print("Case #1:")
while i<j and k <=fin:
    [fl, de]=f(s)
    if fl:
        i+=1
        print(s,end=' ')
        for g in de:
            print(g, end=' ')
        print()
    s=bin1(s)
    k=int(s,2)
