import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    i = 1
    while i <= t:
        ans = 0
        line = sys.stdin.readline()
        l = len(line)
        p = line[0]
        for j in xrange(1, l-1):
            if p != line[j]:
                ans += 1
                p = line[j]
        if p == '-':
            ans += 1
        print 'Case #%d: %d' % (i, ans)
        i += 1
