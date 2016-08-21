from string import uppercase
import sys
import itertools

def no_majority(nums):
    total = sum(nums) * 1.0
    if total == 0:
        return True
    for num in nums:
        if num / total > 0.5:
            return False
    return True

def get_indexes(indexes):
    for a, b in itertools.permutations(indexes,r=2):
        yield a,b
    for index in indexes:
        yield index

def get_step(parties):
    indexes = [i for (i,n) in enumerate(parties) if n]
    for a, b in itertools.permutations(indexes,r=2):
        step = [None, None]
        remaining_senators = parties[:]
        if remaining_senators[a]:
            step[0] = a
            remaining_senators[a] -= 1
        if remaining_senators[b]:
            step[1] = b
            remaining_senators[b] -= 1
        if no_majority(remaining_senators):
            return step
    return None, parties.index(max(parties))

for case_num in xrange(1,int(raw_input()) + 1):
    raw_input()
    in_parties = map(int, raw_input().split(" "))
    plan = []
    while sum(in_parties) > 0:
        a,b = get_step(in_parties)
        plan.append("".join([uppercase[n] for n in (a,b) if n is not None]))
        if a is not None:
            in_parties[a] -= 1
        if b is not None:
            in_parties[b] -= 1
    print "Case #%s: %s" % (case_num, " ".join(plan))



