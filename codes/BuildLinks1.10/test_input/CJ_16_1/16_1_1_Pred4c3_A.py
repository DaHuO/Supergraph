T=int(input())
for case_id in range(1,T+1):
    S=input()
    def solve():
        res = S[0]
        for i in range(1,len(S)):
            if ord(S[i]) >= ord(res[0]):
                res = S[i]+res
            else:
                res = res+S[i]
        return res

    ans = solve()
    print('Case #%d: %s' % (case_id, ans))
    import sys
    print('Case #%d: %s' % (case_id, ans), file=sys.stderr)
