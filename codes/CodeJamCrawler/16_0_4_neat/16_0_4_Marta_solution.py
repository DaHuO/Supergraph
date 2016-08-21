T = input()
for i in range(T):
    K,C,S = map(int,raw_input().split())

    if K/C > S:
        sol = 'IMPOSSIBLE'
    else:
        pos = []
        j = 0
        while j < K:
            pos += [sum(min(j+i,K-1)*K**i for i in range(C))+1]
            j += C

        sol = ' '.join(map(str,pos))

    print 'Case #'+str(i+1)+": " + sol
