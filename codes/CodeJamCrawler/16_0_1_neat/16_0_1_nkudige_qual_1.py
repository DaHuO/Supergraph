def digits(x):
    while x != 0:
        yield x % 10
        x /= 10

def bleatrix_sleepat(N):
    if N == 0:
        return 'INSOMNIA'

    n, i = N, 1

    hashmap = {
        0: True,
        1: True,
        2: True,
        3: True,
        4: True,
        5: True,
        6: True,
        7: True,
        8: True,
        9: True,
    }

    while hashmap:
        for d in digits(n):
            hashmap.pop(d, None)
        if not hashmap:
            return n

        i += 1
        n = N * i

T = int(raw_input())

for i in xrange(1, T+1):
    N = int(raw_input())
    print 'Case #%d: %s' % (i, bleatrix_sleepat(N))