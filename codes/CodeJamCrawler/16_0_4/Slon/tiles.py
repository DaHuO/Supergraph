import sys

T=int(sys.stdin.readline().strip())

for k in range(1, T + 1):
    K, C, S = map(int, sys.stdin.readline().strip().split())
    print("Case #%d: %s" % (k, " ".join(map(str, range(1, K + 1)))))
