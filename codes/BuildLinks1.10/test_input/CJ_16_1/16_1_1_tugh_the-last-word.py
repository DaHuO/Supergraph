T = int(input())

for t in range(1, T+1):
    S = input()
    ans = S[0]

    for c in S[1:]:
        if c >= ans[0]:
            ans = c + ans
        else:
            ans += c

    print("Case #%d: %s" % (t, ans))        