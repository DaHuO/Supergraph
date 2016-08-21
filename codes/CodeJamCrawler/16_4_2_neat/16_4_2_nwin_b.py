from random import shuffle
def solve():
    n, k = map(int, raw_input().split())
    p = map(float, raw_input().split())
    p.sort()
    ans = 0
    for t in xrange(k + 1):
        q = p[:t]
        if t != k:
            q += p[-k+t:]
        shuffle(q)
        dp = [0] * (k + 1)
        dp[0] = 1
        for j, x in enumerate(q):
            for i in xrange(j + 1, 0, -1):
                dp[i] = dp[i] * (1 - x) + dp[i-1] * x
            dp[0] = dp[0] * (1 - x)
        if ans < dp[k/2]:
            ans = dp[k/2]
    return ans

T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %.12f" % (t + 1, solve())
