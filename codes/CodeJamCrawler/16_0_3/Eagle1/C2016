T=int(input())
for t in range(0,T):
    N, J = [int(x) for x in input().split()]
    print("Case #%d:"%(t+1))
    M=30030
    B = [0 for x in range(M+1)]
    for p in [ 2, 3, 5, 7, 11, 13 ]:
        for x in range(p, M+1, p):
            B[x] = p
    Z = [[0 for i in range(N+1)] for j in range(11)]
    for m in range(2,11):
        Z[m][N-1]=1
        for b in range(N-2,-1,-1):
            Z[m][b]=(Z[m][b+1]*m)%M
    j = 0
    low=2**(N-1)+1
    high=2**N
    #print("J=%d low=%s high=%s"%(J,bin(low),bin(high)))
    for i in range(low,high,2):
        if B[i%M]>0:
            S=bin(i)[2:]
            V = [0 for x in range(11)]
            V[2]=B[i%M]
            failed=0
            for m in range(3,11):
                l=0
                L=0
                for b in range(0,N):
                    L=L*m
                    if S[b]=='1':
                        l+=Z[m][b]
                        L+=1
                if B[l%M]>0:
                    V[m]=B[l%M]
                    #print("%s %d %d %d %d"%(S,m,L,l,V[m]))
                else:
                    failed=1
                    break
            if failed==0:
                print(S,V[2],V[3],V[4],V[5],V[6],V[7],V[8],V[9],V[10])
                j+=1
                if j>=J:
                    break
