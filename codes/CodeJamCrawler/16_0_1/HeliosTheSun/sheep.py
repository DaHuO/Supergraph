import fileinput
test_file = fileinput.input()
num_tests = int(next(test_file).strip())
for i in xrange(num_tests):
    n = int(next(test_file).strip());
    if 0 == n:
        print "Case #%d: INSOMNIA" % (i + 1)
    else:
        all_digits = set([ j for j in range(10) ])
        digits = set()
        j = 1
        while True:
            num = n * j
            for c in str(num):
                digits.add(int(c))
            if digits == all_digits:
                break
            else:
                j += 1
        print "Case #%d: %d" % (i + 1, n * j)
