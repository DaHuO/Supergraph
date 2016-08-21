import sys

def print_answer(N, case):
        visible_chars = set()
        if N == 0:
            print 'Case #%d: INSOMNIA' % case
            return
        current = N
        tries = 0
        while not visible_chars.issuperset(('0','1','2','3','4','5','6','7','8','9')):
            tries += 1
            current = tries * N
            visible_chars.update(str(current))

        print "Case #%d: %d" % (case, current)

lines = sys.stdin.readlines()
test_cases = int(lines[0])
for i in xrange(1, test_cases+1):
    N = int(lines[i])
    print_answer(N, i)