def solve():
    num = int(raw_input())
    if num == 0:
        return 'INSOMNIA'
    dig = set(list(str(num)))
    ans = num
    while len(dig) < 10:
        ans += num
        dig.update(list(str(ans)))
    return ans

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)