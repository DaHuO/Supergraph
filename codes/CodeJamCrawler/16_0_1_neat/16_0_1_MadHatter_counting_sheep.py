num_test_cases = int(raw_input().strip(" "))

for case in xrange(1, num_test_cases + 1):
    n = int(raw_input().strip(" "))
    s = set([])
    asleep = False
    for force in xrange(1, 10000):
        num = force * n
        for c in str(num):
            s.add(c)
        if len(s) == 10:
            print "Case #%d: %d" % (case, num)
            asleep = True
            break
    if not asleep:
        print "Case #%d: INSOMNIA" % case

