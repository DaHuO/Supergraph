import math

def number_of_tiles(k, c):
    return k - c + 1 if k > c else 1

def key_tiles(k, c, nt):
    arg = min(k, c)
    return ['1'] + [str(p*k + (p+2)) for p in range(arg - 1 + nt - 1)]

t = int(raw_input())
for i in range(t):

    k, c, s = map(int, raw_input().strip().split(' '))
    print "Case #{0}:".format(i+1),

    print ' '.join(map(str, range(1, s+1)))
    continue

    nt = number_of_tiles(k, c)
    print "Number : {0}".format(nt)
    print key_tiles(k, c, nt)
    continue

    if nt > s:
        print "IMPOSSIBLE"
        continue

    if c == 1:
        print ' '.join(map(str, range(1, k+1)))
    elif k == 1:
        print '1'
    else:
        print ' '.join(key_tiles(k, c, nt)[-nt:])
