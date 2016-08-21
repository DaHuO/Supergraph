# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
def maxima(D):
    max  = None
    min = None
    for i in D.keys():
        if max == None:
            max = i
        if min == None:
            min = i
        if D[max]<=D[i]:
            max = i
        if D[min]>=D[i]:
            min = i

    if D[min]==D[max] or D[min]==0:
        flag = 'Equal'
    else: flag = 'NE'
    return max, flag



L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
B = []
T = int(input())
for _ in range(T):
    n = int(input())
    count = -1
    D = {}
    for i in input().split():
        count +=1
        D[L[count]]=int(i)

    print('Case #{}: '.format(_+1), end='')
    while sum(D.values())>2:
        print(' ', end='')
        S, flag = maxima(D)
        # print(S, flag)
        print(S, end = '')
        D[S]=D.get(S)-1
        S, flag= maxima(D)
        # print('','here', S, flag)
        if flag!='Equal':

            print(S, end='')

            # print(D, S, flag)
            D[S] = D.get(S) - 1
        print('',end= '')

    print(' ', end='')
    for kw in D.keys():
        if D[kw]>0:
            print(kw, end = '')
    print('')







