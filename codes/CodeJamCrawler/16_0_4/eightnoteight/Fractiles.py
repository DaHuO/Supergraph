def main():
    for t in xrange(1, 1 + int(raw_input())):
        k, c, s = map(int, raw_input().split())
        print 'Case #%s: %s' % (t, ' '.join(map(str, xrange(1, s + 1))))

main()
