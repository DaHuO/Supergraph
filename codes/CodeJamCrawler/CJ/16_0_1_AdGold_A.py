def last(n):
    if n == 0:
        return 'INSOMNIA'
    got = set()
    x = 0
    while len(got) < 10:
        x += n
        got = got | set(str(x))
    return x

#  inp = map(int, list(open('a-sample.in'))[1:])
#  inp = map(int, list(open('A-small-attempt0.in'))[1:])
inp = map(int, list(open('A-large.in'))[1:])
for t, n in enumerate(inp):
    print 'Case #%d: %s' % (t+1, last(n))
