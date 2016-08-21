T = int(raw_input())

N, J = map(int, raw_input().split())

print 'Case #1:'

start = 1 + (1 << (N - 1))
ans = 0
while ans < J:
    s = bin(start)[2:]
    t = [list(factor(int(s, i))) for i in xrange(2, 11)]
    start += 2
    if 1 in map(len, t):
        continue
    print s, ' '.join([str(x[0][0]) for x in t])
    ans += 1