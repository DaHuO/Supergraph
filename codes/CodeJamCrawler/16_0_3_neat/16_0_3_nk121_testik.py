from math import *
import sys
sys.stdin = open("a.txt")
sys.stdout = open("tmp.txt", "w")
tttt = int(input())
tmptmptmp = list(map(int, input().split()))
i = 2 ** 15 + 1
jj = 0
ans = []
while i < 2 ** 16 and jj < 50:
    #print("a")
    msk = []
    ni = i
    for j in range(16):
        msk.append(ni % 2)
        ni //= 2
    tmp = []
    for j in range(2, 11):
        tt = 0
        for k in range(16):
            tt += j ** k * msk[k]
        ii = 2
        while ii <= (tt ** 0.5):
            if tt % ii == 0:
                break
            ii += 1
        if tt % ii == 0:
            tmp.append(ii)
        else:
            break
    if len(tmp) == 9:
        ans.append([msk] + tmp)
        jj += 1        
    i += 2
for i in range(50):
    print(*reversed(ans[i][0]), sep="", end=" ")
    print(*ans[i][1:])