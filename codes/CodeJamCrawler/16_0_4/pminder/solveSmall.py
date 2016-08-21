T = int(raw_input())


def solve():
    K, C, S = raw_input().split(' ')
    K, C, S = int(K), int(C), int(S)

    if K != S:
        return "IMPOSSIBLE"

    return " ".join("{}".format(i) for i in range(1, K+1))

for t in range(T):
    print "Case #{}: ".format(t+1) + solve()
