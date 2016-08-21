def solve():
    K, C, S = map(int, raw_input().split())
    if C == 1:
        return ' '.join(map(str, range(1, K+1)))
    elif K == 2:
        return 2
    elif K == S:
        return ' '.join(map(str, range(1, K+1)))
    return 0

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)