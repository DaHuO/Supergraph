#!/usr/bin/python3
# Algorithm: change the leftmost group to match the next one:
# -+-+- (5 groups)
# ++-+-
# ---+-
# ++++-
# -----
# +++++ (5 movements)
# So you just need to count the number of groups (not counting the ending +)

import sys

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    s = sys.stdin.readline().strip()

    groups = 0
    grouptype = None
    for pancake in s:
        if pancake != grouptype:
            groups += 1
            grouptype = pancake

    if grouptype == '+':
        groups -= 1

    print("Case #{0}: {1}".format(t, groups))

