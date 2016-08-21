from math import log

for case in range(1, int(input())+1):
    K, C, S = map(int ,input().strip().split(" "))
    if log(K, 2) - log(S, 2) > C-1:
        print('Case #'+str(case)+": IMPOSSIBLE")
    else:
        tmp = list(range(1, K+1))
        print('Case #'+str(case)+": "+' '.join([str(i) for i in tmp]))

