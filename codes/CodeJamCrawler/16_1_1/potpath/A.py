T = int(input())
for t in range(1, T + 1):
    print('Case #%d: ' % t, end='')
    s = input()
    ans = s[0]
    for i in s[1:]:
        if i < ans[0]:
            ans = ans + i
        else:
            ans = i + ans
    print(ans)
