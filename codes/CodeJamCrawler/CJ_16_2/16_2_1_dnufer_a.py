import sys
from collections import defaultdict

DIGITS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

#DIGITS = ("ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE")

# def solve(counts, n):
#     for c in n:
#         if counts[c] == 0:
#             return None
#         else:
#             counts[c] -= 1
#
#     done = True
#     for c in counts:
#         done = done and counts[c] == 0
#
#     ii = DIGITS.index(n)
#     if done:
#         return str(ii)
#     else:
#         for nn in DIGITS[ii:]:
#             a = solve(counts.copy(), nn)
#             if a is not None:
#                 return str(ii) + a
#             else:
#                 pass
#
#
# T = int(sys.stdin.readline())
#
# for t in xrange(T):
#     s = sys.stdin.readline().strip()
#
#     counts = defaultdict(int)
#     for c in s:
#         counts[c] += 1
#
#     result = None
#     for i, n in enumerate(DIGITS):
#         result = solve(counts.copy(), n)
#         if result is not None:
#             break
#
#     print "Case #%d:" % (t + 1), result


T = int(sys.stdin.readline())

for t in xrange(T):
    s = sys.stdin.readline().strip()

    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    result = ''

    result += counts['Z'] * '0'
    for x in xrange(counts['Z']):
        for c in DIGITS[0]:
            counts[c] -= 1

    result += counts['W'] * '2'
    for x in xrange(counts['W']):
        for c in DIGITS[2]:
            counts[c] -= 1

    result += counts['U'] * '4'
    for x in xrange(counts['U']):
        for c in DIGITS[4]:
            counts[c] -= 1

    result += counts['X'] * '6'
    for x in xrange(counts['X']):
        for c in DIGITS[6]:
            counts[c] -= 1

    result += counts['G'] * '8'
    for x in xrange(counts['G']):
        for c in DIGITS[8]:
            counts[c] -= 1

    result += counts['O'] * '1'
    for x in xrange(counts['O']):
        for c in DIGITS[1]:
            counts[c] -= 1

    result += counts['H'] * '3'
    for x in xrange(counts['H']):
        for c in DIGITS[3]:
            counts[c] -= 1

    result += counts['F'] * '5'
    for x in xrange(counts['F']):
        for c in DIGITS[5]:
            counts[c] -= 1

    result += counts['V'] * '7'
    for x in xrange(counts['V']):
        for c in DIGITS[7]:
            counts[c] -= 1

    result += counts['E'] * '9'
    for x in xrange(counts['E']):
        for c in DIGITS[9]:
            counts[c] -= 1

    print "Case #%d:" % (t + 1), ''.join(sorted(result))
