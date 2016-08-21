t = int(raw_input())
for i in range(t):
    s = raw_input()
    pre = '#'
    ans = 0
    for c in s:
        if (c != pre):
            pre = c
            ans += 1
    if (s[-1] == '+'):
        ans -= 1
    print "Case #{}: {}".format(i + 1, ans)
