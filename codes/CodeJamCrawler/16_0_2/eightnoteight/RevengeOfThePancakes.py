from itertools import groupby

def main():
    for t in xrange(1, 1 + int(raw_input())):
        print 'Case #%d: %d' % (t, len(list(groupby(raw_input().rstrip('+')))))

main()

