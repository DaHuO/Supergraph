def done(p):
    return all(x == 0 for x in p)


def parties_remaining(p):
    return [x for x in range(len(p)) if p[x] != 0]


def remove(param, p):
    ret = list(p)
    for removal in param:
        ret[removal] -= 1
    return ret


def possible_removals(p):
    removing_one = parties_remaining(p)
    ret = []
    for party in removing_one:
        left = remove([party], p)
        for x in parties_remaining(left):
            ret.append([party, x])
    ret.extend([[x] for x in removing_one])
    return ret


def no_majority(param):
    return all([x == 0 for x in param]) or all([float(x)/sum(param) <= 0.5 for x in param])


def solve(p):
    if(done(p)):
        return []
    for removal in possible_removals(p):
        if no_majority(remove(removal, p)):
            return [removal] + solve(remove(removal, p))



cases = int(raw_input())


def output(param):
    for line in param:
        sys.stdout.write("".join(map(lambda x: chr(x+ord('A')), line)))
        sys.stdout.write(" ")

import sys
for case in xrange(cases):
    n = int(raw_input())
    p = map(int, raw_input().split())
    sys.stdout.write("Case #%d: " % (case + 1))
    output(solve(p))
    print