import sys
import collections


def flip(s, n):
    return tuple(reversed(['+' if t == '-' else '-' for t in s[:n]])) + s[n:]


def find_answer(s):
    q = collections.deque([(s, 0)])
    states = set()
    chars = len(s)
    perfect = tuple('+' * chars)
    while q:
        current_stack, attempt = q.popleft()
        if current_stack == perfect:
            return attempt
        for i in xrange(1, chars+1):
            flipped = flip(current_stack, i)
            if flipped not in states:
                states.add(flipped)
                q.append((flipped, attempt+1))


def print_answer(s, case):
        print "Case #%d: %d" % (case, find_answer(tuple(s[:-1])))

lines = sys.stdin.readlines()
test_cases = int(lines[0])
for i in xrange(1, test_cases+1):
    print_answer(lines[i], i)
