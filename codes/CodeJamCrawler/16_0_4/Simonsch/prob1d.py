import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    print("Case #{}:".format(t), end="")
    line = sys.stdin.readline()
    (K, C, S) = map(int, line.split(' '))
    if (S * C < K):
        print(" IMPOSSIBLE")
        continue
    k = 0
    while k < K:
        query = 1
        for i in range(0, min(C, K-k) ):
            query += k * (K ** i)
            k += 1
        print(" {}".format(query), end="") 
    print("")


