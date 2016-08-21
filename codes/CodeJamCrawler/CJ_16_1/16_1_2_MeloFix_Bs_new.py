T = int(input())

for loopC in range(1,T+1):

    N = int(input())

    S = [list(map(int,input().split())) for x in range(2*N-1)]

    '''
    Ssave = S[:]
    
    L = []
    for x in range(N):
        L.append([None]*N)

    Ls = []
    missingnum = 0
    
    for turn in range(N):
        S.sort(key=lambda x:x[turn])

        tmp = S[:2]
        if len(tmp)!=1 and tmp[0][turn] == tmp[1][turn]:
            Ls.append(S[:2])
            S.pop(0)
            S.pop(0)
        else:
            missingnum = turn
            Ls.append(S[:1])
            S.pop(0)

    Ssave.sort()
    for x in Ssave:
        print(x)

    
    L[0] = Ls[0][0]
    Ls[0].pop(0)
    '''

    L =[0]*2600

    for x in S:
        for y in x:
            L[y] += 1

    ret = []
    for x in range(len(L)):
        if L[x] != 0 and L[x]%2 != 0:
            ret.append(x)
            #print(x,L[x],ret)
            
    rets = ''
    for x in ret:
        rets = rets+str(x)+' '
        
    print("Case #{}: {}".format(loopC,rets))
        
