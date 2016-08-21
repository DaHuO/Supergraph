import sys

def solve(f):
    n = int(f.readline())
    if n == 0:
        print 'INSOMNIA'
        return
    mask = {}
    m = 0
    i = 1
    while i < 1000000:
        for c in list(str(n * i)):
            if not mask.has_key(c):
                mask[c] = True
                m = m + 1
                if m >= 10:
                    print n * i
                    return
        i = i + 1
    print 'INSOMNIA'

if __name__ == "__main__":
   f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
   t = int(f.readline())
   for i in range(1, t + 1):
       print 'Case #%d:' % (i),
       solve(f)
