
import sys

def getM(K,C):
    L = list(range(0,C))
    #print(L)
    s = sum([K**p for p in L])
    return s #print(s)



T = int(input())
print('|T:',T)
for i in range(1,T+1):
    def _():
        print()
        K,C,S = (int(_) for _ in input().split())
        print('| K:{K} C:{C} S:{S}'.format(K=K,C=C,S=S))
        if( S < K ):
            print('Case #%d: IMPOSSIBLE')
        else:
            # S >= K
            M = getM(K=K,C=C)
            print('M:',M)
            L = []
            for k in range(K):
                L += ['%s' % (1+M*k) ]
            print('Case #%d:' % i, ' '.join(L))
    _()

