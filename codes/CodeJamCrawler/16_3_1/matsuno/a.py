import sys
import string

ALPHA = string.ascii_uppercase

def do(N, P):
    m = []
    s = 0
    for i in xrange(N):
        p = int(P[i])
        m.append([ALPHA[i], p])
        s += p

    i = 0
    while i < s:
        sys.stdout.write(" ")

        m = sorted(m, cmp=lambda x, y: cmp(x[1], y[1]))
        m[-1][1] -= 1
        i += 1
        sys.stdout.write(m[-1][0])

        m = sorted(m, cmp=lambda x, y: cmp(x[1], y[1]))
        if  m[-1][1] - 1 < (s - i - 1 + 1) >> 1:
            continue
        m[-1][1] -= 1
        i += 1
        sys.stdout.write(m[-1][0])
    print


def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline().strip())
        P = sys.stdin.readline().strip().split()
        print "Case #{0}:".format(t + 1),
        do(N, P)

if __name__ == '__main__':
    main()
