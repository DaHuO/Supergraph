def solve(x):
    if x[-1] != '+':
        x += '+'
    l = len(x)
    ans = 0
    for i in range(1, l):
        if x[i] != x[i - 1]:
            ans += 1
    return ans

t = int(input())

for i in range(t):
    x = input()
    print('Case #%d: %s' % (i + 1, solve(x)))
