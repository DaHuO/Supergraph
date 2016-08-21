for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print('Case #{}: {}'.format(_+1,'INSOMNIA'))
        continue

    L = [0,1,2,3,4,5,6,7,8,9]
    k = 1
    while True:
        n = map(int,list(set(str(k*N))))
        #print k,N,L,n,len(L)
        #print L
        for i in n:
            #print i
            if L.count(i) != 0:
                L.remove(i)
        #print k*N,L
        #print '##########################################'
        if len(L) == 0:
            break
        k += 1
    print('Case #{}: {}'.format(_+1,k*N))