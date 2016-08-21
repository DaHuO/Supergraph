T = int(raw_input())

all_digits = set(map(int, '0123456789'))

def digits(n):
    return set(map(int, str(n)))

def last_number(n):
    if n == 0:
        return None

    x = 0
    ds = set()
    while len(ds) < len(all_digits):
        x += n
        ds = ds.union(digits(x))
    return x

for t in range(T):
    n = int(raw_input())
    s = last_number(n)
    if s is None:
        print 'Case #%d: INSOMNIA' % (t + 1)
    else:
        print 'Case #%d: %d' % (t + 1, s)

