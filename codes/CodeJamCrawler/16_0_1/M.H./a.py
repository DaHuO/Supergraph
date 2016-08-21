def good(m):
    for c in range(10):
        if not c in m:
            return False
    return True

def digits(n):
    return set(map(lambda x: int(x), str(n)))

T = int(input().strip())
for casen in range(1, T + 1):
    x = int(input().strip())
    if x == 0:
        print('Case #%d: INSOMNIA' % (casen, ))
    else:
        c = x
        digs = digits(c)
        while not good(digs):
            c += x
            digs.update(digits(c))
        print('Case #%d: %d' % (casen, c))
