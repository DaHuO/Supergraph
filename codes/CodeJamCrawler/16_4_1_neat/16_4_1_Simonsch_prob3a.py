import sys
import math
import numpy as np


def num_to_chr(i):
    if i == 0:
        return 'P'
    elif i == 1:
        return 'R'
    else :
        return 'S'

T = int(sys.stdin.readline())
for t in range(1, T+1):
    line = sys.stdin.readline()
    (N, R, P, S) = map(int, line.split(' '))
    NN = 2 ** N
    
    found = False
    s = np.zeros(NN)
    for c in range(3):
        s[0] = c
        n = 1
        while n < NN:
            for i in range(n):
                index = i*(NN // n)
                s[index + (NN // (2*n))] = (s[index]+1) % 3 
            n = 2 * n
        if (np.count_nonzero(s == 0) == P) and (np.count_nonzero(s == 1) == R):
            found = True
            break

    if found == False:
        print("Case #{}: ".format(t), end="")
        print("IMPOSSIBLE")
        continue
    sl = s.tolist()
    n = 1
    while n < NN:
        i = 0
        while i < NN:
            if sl[i:(i+n)] > sl[(i+n):(i+2*n)]:
                h = sl[i:(i+n)]
                sl[i:(i+n)] = sl[(i+n):(i+2*n)]
                sl[(i+n):(i+2*n)] = h
            i = i+2*n
        n = 2*n
    so = ''.join(num_to_chr(i) for i in sl)
    print("Case #{}: ".format(t), end="")
    print(so)



