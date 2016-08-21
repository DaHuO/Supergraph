def get_digits(x):
    d = []
    while x > 0:
        d.append(x % 10)
        x /= 10
    return set(d)

def get_num(x):
    s = set()
    y = x
    while True:
        s = s.union(get_digits(y))
        if len(s) == 10:
            return y
        y += x

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    if n == 0:
        print 'Case #%d: INSOMNIA' % (i + 1)
    else:
        print 'Case #%d: %d' % (i + 1, get_num(n))
