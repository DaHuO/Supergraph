def main():
    T = int(raw_input())
    for i in xrange(T):
        N = int(raw_input())
        if N == 0:
            output(i+1, 'INSOMNIA')
            continue
        s = set()
        k = 1
        while True:
            n = N * k
            s.update(list(str(n)))
            if len(s) == 10:
                output(i+1, n)
                break
            k += 1

def output(casenum, ret):
    print 'Case #%d: %s' % (casenum, ret)


main()
