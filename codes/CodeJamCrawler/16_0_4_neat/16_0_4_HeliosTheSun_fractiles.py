import fileinput
test_file = fileinput.input()
num_tests = int(next(test_file).strip())
for i in xrange(num_tests):
    line = next(test_file).split(" ")
    K = int(line[0].strip())
    C = int(line[1].strip())
    S = int(line[2].strip())
    result = " ".join(str(j + 1) for j in xrange(K))
    print "Case #%d: %s" % (i + 1, result)
