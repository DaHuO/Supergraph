import sys
import string
import re

T = int(input())

for i in range(1, T + 1):
    k, c, s = map(int, input().split(" "))

    kc = pow(k, c)
    l = ['1']
    for j in range(kc//k+1, kc+1, kc//k):
        l.append(str(j))

    print("Case #{}: {}".format(i, " ".join(l)))
