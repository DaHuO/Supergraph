T = input()

for k in range(T):
    s = raw_input()

    ans = s[0]

    for i in range(1, len(s)):
        if s[i] >= ans[0]:
            ans = s[i] + ans
        else:
            ans = ans + s[i]

    print "Case #%d: "%(k+1) + ans
