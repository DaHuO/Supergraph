import sys
import os
from collections import defaultdict

f = sys.stdin
# f = open('/tmp/A-small-attempt0.in', 'r')

DEC = [
    ("Z", "ZERO", 0),
    ("W", "TWO", 2),
    ("G", "EIGHT", 8),
    ("T", "THREE", 3),
    ("R", "FOUR", 4),
    ("X", "SIX", 6),
    ("O", "ONE", 1),
    ("F", "FIVE", 5),
    ("S", "SEVEN", 7),
    ("I", "NINE", 9),
]

tests = int(f.readline())

for t in range(1, tests+1):
    lets = f.readline().strip()
    cnts = defaultdict(int)

    for c in lets:
        cnts[c] += 1

    phone = ''
    for x, rems, dig in DEC:
        n = cnts[x]
        for r in rems:
            cnts[r] -= n
        phone += str(dig) * n


    phone = ''.join(sorted(phone))

    print "Case #%d: %s" % (t, phone)





