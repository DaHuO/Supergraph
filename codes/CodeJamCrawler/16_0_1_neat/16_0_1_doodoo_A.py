def digits(num):
    ret = []
    while num > 0:
        ret.insert(0, num %10)
        num /= 10

    return ret

def solve(N):
    if N == 0:
        return 'INSOMNIA'

    last = N
    i = 1
    digs = set(digits(last))

    while len(digs) < 10:
        i += 1
        last = N*i
        digs |= set(digits(last))

    return last

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    print 'Case #%d: %s' % (i + 1, solve(N))
