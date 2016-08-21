INPUT = "1-large"

f = open('%s.in' % INPUT, 'r')
o = open('%s.out' % INPUT, 'w')

T = int(f.readline().strip())


def solve(n):
    if n == 0:
        return "INSOMNIA"

    digits = set()
    i = 1
    last_number = 0
    while len(digits) < 10:
        last_number = n * i
        digits.update([int(x) for x in str(last_number)])
        i += 1

    return last_number

for t in xrange(T):

    n = int(f.readline().strip())

    res = solve(n)
    s = "Case #%d: %s\n" % (t+1, res)
    o.write(s)

f.close()
o.close()
