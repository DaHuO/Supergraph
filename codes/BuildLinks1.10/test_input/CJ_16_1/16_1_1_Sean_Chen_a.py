def solve(s):
    ans = []
    max = s[0]
    ans.append(max)

    for c in s[1:]:
        if c >= max:
            ans.insert(0, c)
            max = c
        else:
            ans.append(c)

    return ans

T=int(raw_input())
for cas in xrange(1,T+1):
    S=str(raw_input())
    ans = solve(S)
    print "Case #{}: {}".format(cas,"".join(map(str, ans)))



