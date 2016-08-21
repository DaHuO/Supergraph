T = int(input())
for test in range(1, T + 1):
    K, C, S = [int(x) for x in input().split()]
    print("Case #%d: %s" % (test, " ".join([str(x) for x in range(1, K + 1)])))
