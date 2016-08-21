# python3
import math

def convert(s):
    if s=='PR' or s=='RP':
        return 'P'
    elif s=='PS' or s=='SP':
        return 'S'
    elif s=='RS' or s=='SR':
        return 'R'
    else:
        print('ERROR', s)
        return 'P'
        
def order(up,low, n, lis):
    if n == 0:
        return up[0]
    nup=[]
    nlow=[]
    if len(up) == 1:
        if 'P'==up[0]:
            nup=['P','S']
            nlow=['R']
        if 'R'==up[0]:
            nup=['R','P']
            nlow=['S']
        if 'S'==up[0]:
            nup=['R','S']
            nlow=['P']
    elif len(low)==1:
        if 'P'==low[0]:
            nlow=['P','S']
            nup=['R']
        if 'R'==low[0]:
            nlow=['R','P']
            nup=['S']
        if 'S'==low[0]:
            nlow=['R','S']
            nup=['P']
           
    strin = order(nup,nlow,n-1,''.join([convert(e) for e in [lis[0:2], lis[0] + lis[2], lis[1:]] ]) )
    return replace(strin, lis)

def replace(s, lis):
    news=''
    subst=[lis[0:2],lis[1:], lis[0] + lis[2]]
    for j in range(len(s)):
        if s[j] == 'P':
            if 'PR' in subst:
                news += 'PR'
            else:
                news += 'RP'
        elif s[j] == 'S':
            if 'PS' in subst:
                news += 'PS'
            else:
                news += 'SP'
        else:
            if 'RS' in subst:
                news += 'RS'
            else:
                news += 'SR'
    return news
        
            
    
def solve():
    N,R,P,S= [int(e) for e in input().split()]
    up = math.ceil(2**N/3)
    low = math.floor(2**N/3)

    if R < low or R > up:
        return 'IMPOSSIBLE'
    if P < low or P > up:
        return 'IMPOSSIBLE'
    if S < low or S > up:
        return 'IMPOSSIBLE'

    nup=[]
    nlow=[]
    if P == up:
        nup.append('P')
    else:
        nlow.append('P')
    if R == up:
        nup.append('R')
    else:
        nlow.append('R')
    if S == up:
        nup.append('S')
    else:
        nlow.append('S')

    return order(nup ,nlow, N, 'PRS' )
 
T=int(input());
 
for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())
