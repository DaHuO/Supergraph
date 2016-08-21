test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = int(raw_input())
    s = str(n)
    m = n
    if n == 0:
        print "Case #{}: {}".format(case, "INSOMNIA")
        continue
    while True:
        for i in s:
            if i in a:
                a.remove(i)
        #print n, len(a)
        if len(a) == 0:
            print "Case #{}: {}".format(case, str(m))
            break
        m += n
        s = str(m)