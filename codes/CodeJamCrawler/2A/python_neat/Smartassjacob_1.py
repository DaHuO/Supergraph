import math
input=open('1in','r')
output=open('1out','w')
T=int(input.readline())
g={}
def w(c):
    if c=='R':
        return 'S'
    if c=='S':
        return 'P'
    if c=='P':
        return 'R'
def f(N, c):#length N, with c as the winner. returns shortest string.
    if (N,c) in g:
        return g[(N,c)]
    if N==0:
        return c
    else:
        s1=f(N-1,c)
        s2=f(N-1,w(c))
        A=[s1,s2]
        A.sort()
        g[(N,c)]=A[0]+A[1]
        return g[(N,c)]
for dummy in range(T):
    print dummy+1
    output.write('Case #'+str(dummy+1)+': ')
    [N,R,P,S]=[int(x) for x in input.readline().split()]
    s1=f(N,'P')
    s2=f(N,'R')
    s3=f(N,'S')
    if s1.count('R')==R and s1.count('S')==S and s1.count('P')==P:
        output.write(s1+'\n')
    elif s2.count('R')==R and s2.count('S')==S and s2.count('P')==P:
        output.write(s2+'\n')
    elif s3.count('R')==R and s3.count('S')==S and s3.count('P')==P:
        output.write(s3+'\n')
    else:
        output.write('IMPOSSIBLE\n')

    
                 
