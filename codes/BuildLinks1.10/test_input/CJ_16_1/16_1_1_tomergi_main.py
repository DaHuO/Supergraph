import sys

def find_answer(s):
    current = ""

    for i in s:
        if not current:
            current += i
        elif i >= current[0]:
            current = i + current
        else:
            current += i
    return current


def print_answer(s, case):
    print "Case #%d: %s" % (case, find_answer(s))


lines = sys.stdin.readlines()
test_cases = int(lines[0])
for i in xrange(1, test_cases+1):
    print_answer(lines[i].rstrip(), i)