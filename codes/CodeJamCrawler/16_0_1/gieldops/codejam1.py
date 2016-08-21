t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
    n = int(raw_input())
    counter = [False] * 10
    for i in xrange(1, 1000000):
        last_number = i * n
        digits = set([int(char) for char in str(last_number)])
        for d in digits:
            counter[d] = True
        if counter == [True] * 10:
            print "Case #%d: %d" % (case, last_number)
            break
    if counter != [True] * 10:
        print "Case #%d: INSOMNIA" % case