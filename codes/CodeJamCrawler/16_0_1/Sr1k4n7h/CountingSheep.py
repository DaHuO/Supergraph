__author__ = 'sr1k4n7h'

for _ in range(int(raw_input().strip())):
    A = range(10)
    N = int(raw_input().strip())
    if N == 0:
        print "Case #{}: INSOMNIA".format(_+1)
    else:
        flag = True
        i = 2
        L = set()
        for j in str(N):
            L.add(int(j))
        K = 0
        while flag:
            K = i * N
            for j in str(K):
                L.add(int(j))
            if list(L) == A:
                flag = False
            i += 1
            # print list(L), K
        print "Case #{}: {}".format(_+1, K)
