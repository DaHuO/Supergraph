def solve(k, c, s):
    return ' '.join(map(str, range(1, s + 1)))

t = int(input())

for i in range(t):
    k, c, s = map(int, input().split())
    print('Case #%d: %s' % (i + 1, solve(k, c, s)))
