import math
input=open('2in','r')
output=open('2out','w')
T=int(input.readline())
def tie(A):#A is an array of probabilities, size of A is even.
#    print A
    B=list(A)
    N=len(B)
    f=[{} for i in range(N+1)]#0 through N
    f[0][0]=1.0
    for j in range(1,N+1):# lets update
        p=B[j-1]
        q=1.0-p
        for v in f[j-1]:
            if v+1 not in f[j]:
                f[j][v+1]=0
            if v-1 not in f[j]:
                f[j][v-1]=0
            f[j][v+1]+=f[j-1][v]*p
            f[j][v-1]+=f[j-1][v]*q
    if 0 not in f[N]:
        f[N][0]=0.0
#    print f[N][0]
    return f[N][0]
for dummy in range(T):
    print dummy+1
    output.write('Case #'+str(dummy+1)+': ')
    [N,K]=[int(x) for x in input.readline().split()]
    A=[float(x) for x in input.readline().split()]
    A.sort()
    final=0.0
    for j in range(0,K+1):
        B=A[:j]+A[N-K+j:]
        final=max(final,tie(B))
    output.write(str("%.8f"%final)+'\n')
                 
