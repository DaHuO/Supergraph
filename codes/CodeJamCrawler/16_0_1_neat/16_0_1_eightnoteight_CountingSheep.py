def main():
    for t in xrange(1, 1 + int(raw_input())):
        n = int(raw_input())
        if n == 0:
            print 'Case #%d: INSOMNIA' % t
        else:
            dig = set()
            for y in xrange(n, 10**9, n):
                dig.update(str(y))
                if len(dig) == 10:
                    print 'Case #%d: %d' % (t, y)
                    break

main()
