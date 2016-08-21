# Red Tape Committee

def process(n, k, p):
    p = sorted(p)
    ret = 0
    for i in range(k + 1):
        ret = max(ret, process2(k, p[:i] + p[n - k + i:]))
    return ret

def process2(k, p):
    dp = [[1]]
    for i in range(len(p)):
        ndp = []
        for y in range(i + 2):
            ndpp = 0
            if y >= 1:
                ndpp += dp[i][y - 1] * p[i]
            if y < len(dp[i]):
                ndpp += dp[i][y] * (1.0 - p[i])
            ndp.append(ndpp)
        dp.append(ndp)
    return dp[-1][k / 2]

cases = int(raw_input())
for case in range(1, cases + 1):
    n, k = map(int, raw_input().split(' '))
    p = map(float, raw_input().split(' '))
    print "Case #" + str(case) + ": %.15f" % (process(n, k, p))
