T = int(input())
for cc in range(1, T + 1):
    s = input()
    ans = s[0]
    for c in s[1:]:
        if c >= ans[0]:
            ans = c + ans
        else:
            ans = ans + c
    print('Case #%d:' % cc , ans)
