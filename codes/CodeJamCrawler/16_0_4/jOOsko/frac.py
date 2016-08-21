import sys

N = int(sys.stdin.readline())

def count(K, C, S):
    if C == 1:
        if S < K:
            yield "IMPOSSIBLE"
        else:
            yield " ".join(map(str, range(1, S+1)))
    elif S < (K+1)//2:
        yield "IMPOSSIBLE"
    else:
        sample_len = K**(C-1)
        for j in range(0, K-1, 2):
            yield sample_len*j + j + 2
        if K % 2:
            yield K**C


for case in range(N):
    K, C, S = map(int, sys.stdin.readline().split())
    print("Case #" + str(case + 1) + ":", " ".join(map(str, count(K, C, S))))    
