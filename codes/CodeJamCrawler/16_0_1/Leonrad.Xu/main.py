import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        s = sys.stdin.readline()[:-1]
        ss = s[0]
        for ch in s[1:]:
            opt1 = ch + ss
            opt2 = ss + ch
            if opt1 > opt2:
                ss = opt1
            else:
                ss = opt2
        print "Case #%s: %s" % (i + 1, ss)
