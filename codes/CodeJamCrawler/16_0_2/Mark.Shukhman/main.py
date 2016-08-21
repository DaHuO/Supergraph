def f(s):
    ans = 1
    s1 = s
    last = s1[0]
    for j in s1:
        if j != last:
            ans += 1
            last = j
    if (last == '+'):
        ans -= 1
    return ans


n = int(input())

ans = []

for i in range(n):
    ans.append('Case #' + str(i + 1) + ': ' + str(f(input())))

for x in ans:
    print(x)