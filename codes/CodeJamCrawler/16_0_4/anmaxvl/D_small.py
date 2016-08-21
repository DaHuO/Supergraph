import sys

def solve(k, c, s):
    pass


if __name__=='__main__':
    T = int(sys.stdin.readline().strip())

    for t in range(T):
        k, c, s = [int(v) for v in sys.stdin.readline().strip().split()]
        print "Case #%d:" % (t+1),
        for i in range(k):
            print i+1,
        print
