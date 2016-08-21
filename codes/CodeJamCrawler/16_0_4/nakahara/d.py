import math


def num(l , length, d):
    res=0
    nl=l
    for j in range(length):
        res+=nl*(d**j)
        nl-=1
    
    return res
    


def solve():
    a=input()
    K=int(a.split()[0])
    C=int(a.split()[1])
    S=int(a.split()[2])

    if S*C < K :
        return 'IMPOSSIBLE'

    res=''
    n=1
    while(n*C < K):
        res+= str(num(n*C-1, C, K) + 1)
        res+=' '
        n+=1

    diff=n*C-K
    temp = num(K-1, C-diff , K)
    res+= str( (temp+1)*(K**diff) )
    
    return res

T=int(input());

for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())