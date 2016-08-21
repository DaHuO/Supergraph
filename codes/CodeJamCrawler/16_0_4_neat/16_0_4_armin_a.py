from sys import stdin as inp

T = int(inp.readline().rstrip())
for cas in range(1, T+1):
    K, C, S = map(int, inp.readline().rstrip().split())
    pos = [i for i in range(K)]
    for i in range(1,C):
        dp = K**i
        for j in range(K):
            pos[j] = pos[j] + j * dp
    print("Case #{0:d}: ".format(cas), end="")
    for i in range(K):
        print(" " + str(pos[i] + 1), end="")
    print()
