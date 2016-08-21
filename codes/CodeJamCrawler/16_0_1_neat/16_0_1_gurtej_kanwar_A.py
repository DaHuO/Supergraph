import sys

def insert_digits(c, seen):
    while (c > 0):
        seen.add(c%10)
        c //= 10

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print "Case #%d: INSOMNIA" % (i+1)
    else:
        seen = set([])
        c = N
        insert_digits(c, seen)
        while len(seen) < 10:
            c += N
            insert_digits(c, seen)
        print "Case #%d: %d" % (i+1, c)
