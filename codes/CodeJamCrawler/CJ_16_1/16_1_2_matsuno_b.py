import sys
from collections import deque

def do(t):
    cnt = {}
    N = int(sys.stdin.readline())
    for i in range(N * 2 - 1):
        for s in sys.stdin.readline().split():
            n = int(s)
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1

    r = []
    for n, c in cnt.iteritems():
        if c & 1 == 1:
            r.append(n)
    r = sorted(r)
    
    print "Case #{0}:".format(t),
    for n in r:
        print "{0}".format(n),
    print

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        do(t + 1)

if __name__ == '__main__':
    main()
