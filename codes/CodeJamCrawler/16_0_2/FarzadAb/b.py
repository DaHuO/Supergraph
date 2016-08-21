T = int(raw_input())

for t in range(T):
    s = raw_input() + '+'
    print('Case #%d: %d' % (t+1, len(filter(lambda tup: tup[0] != tup[1], zip(s[:-1], s[1:])))))
