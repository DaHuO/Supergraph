
import math
from sets import Set

tests = int(raw_input())

def get_set(i, d, k):
    if d == 1:
        return Set([i])
    else:
        return Set([i % k]) | get_set(i / k, d - 1, k)

for t in range(tests):
    print "Case #{}:".format(t+1),

    length, complexity, students = [int(x) for x in raw_input().split(" ")]

    window = length ** (complexity-1)

    remain = Set(range(length))
    res = Set()

    while len(remain) > 0:

        target_i = min(list(remain))

        idxs = range(target_i*window,target_i*window+min(window, 2**10))

        i = min(idxs, key=lambda x: len(remain.difference(get_set(x,complexity,length))))

        covered = get_set(i, complexity, length)
        remain = remain.difference(covered)
        res.add(i+1)

    if len(res) > students:
        print "IMPOSSIBLE"
    else:
        print " ".join([str(x) for x in res])
