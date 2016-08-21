T = int(input())
for t in range(T):
    s = input() + '+'
    print('Case #%d: %d' % (t + 1, s.count('-+') + s.count('+-')))
