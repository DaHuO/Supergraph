import sys
tests = [int(i) for i in open(sys.argv[1]).readlines()[1:]]
for i in xrange(len(tests)):
    print "Case #" + str(i+1) + ":",
    N = tests[i]
    if N == 0:
        print "INSOMNIA"
    else:
        digits = [0 for _ in xrange(10)]
        curr = N
        i = 2
        while True:
            for c in str(curr):
                digits[int(c)] = 1
            if sum(digits) == 10:
                print str(curr)
                break
            curr = N*i
            i += 1