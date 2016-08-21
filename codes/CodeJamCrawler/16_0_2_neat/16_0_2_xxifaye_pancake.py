import sys

def solve():
    p = sys.stdin.readline().strip()
    ret = 0
    for i in xrange(len(p)):
        if i == 0:
            continue
        if p[i] != p[i - 1]:
            ret += 1

    if p[-1] == '-':
        ret += 1

    return ret

if __name__ == '__main__':
    c = int(sys.stdin.readline())
    for i in xrange(c):
        print 'Case #%s: %d' % (i + 1, solve())
