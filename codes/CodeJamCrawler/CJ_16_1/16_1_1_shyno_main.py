import sys
'''
 The Last Word
'''

if __name__ == '__main__':
    f = sys.stdin
    nc = int(f.readline())
    for x in xrange(1, nc+1):
        s = f.readline().strip()
        lw = s[0]
        for c in s[1:]:
            if c >= lw[0]:
                lw = c + lw
            else:
                lw += c
        print "Case #%d: %s" % (x, lw)
