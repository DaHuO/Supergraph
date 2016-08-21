def Int(): return int(raw_input())
def LInt(): return map(int, raw_input().split())
def solve(K, S, C):
    ans = []
    for i in xrange(1, K + 1):
        ans.append(i)
    return ans
T = Int()
for t in range(1, T + 1):
    K, C, S = LInt()
    ans = solve(K, S, C)
    print "Case #{0}: {1}".format(t, ' '.join(map(str, ans)))
