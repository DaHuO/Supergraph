fp=open('A-large.in','r')
P=fp.readlines()
L=len(P)
fp.close()
fout=open('out.out','w')
for t in range(1,L):
    X=int(P[t])
    if X==0:
        fout.write('Case #%d: %s' %(t,'INSOMNIA'))
    else:
        A=[0]*10
        count=0
        N=X
        while count!=10:
            K=N
            while K!=0:
                r=K%10
                if A[r]==0:
                    A[r]=1
                    count+=1
                K=K//10
            N=N+X
        ans=N-X
        fout.write('Case #%d: %d' %(t,ans))
    fout.write('\n')
fout.close()
