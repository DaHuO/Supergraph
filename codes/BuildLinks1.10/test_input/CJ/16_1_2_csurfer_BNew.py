from collections import defaultdict
def solve():
    n = int(input())
    freq = defaultdict(lambda: 0)
    for _ in xrange(2*n - 1):
        for item in map(int, raw_input().split()):
            freq[item] += 1
    ans = []
    for key in freq.keys():
        if freq[key] % 2 != 0:
            ans.append(key)
    return ' '.join(map(str, sorted(ans)))

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)