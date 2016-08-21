
import sys

def solve(n):
    if n == 0:
        return 'INSOMNIA'

    found = {}
    i = 1
    while len(found) < 10:
        num = i * n
        nums = str(num)
        for c in nums:
            found[c] = True
        i += 1
        #print found
    return num

def do_solve(filename):
    with open(filename, 'r') as f:
        num_tests = int(f.readline())
        for i in xrange(num_tests):
            n = int(f.readline())
            num = solve(n)

            print "Case #%d: %s" % (i + 1, num)

do_solve(sys.argv[1])
