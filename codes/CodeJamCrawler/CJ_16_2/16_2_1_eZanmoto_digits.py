import itertools

def sort_str(xs):
    return ''.join(sort(xs))

def sort(xs):
    return list(sorted(xs))


def ps(xs):
    return itertools.chain.from_iterable(itertools.combinations(xs, r) for r in range(len(xs)+1))

def decode(S):
    nums = [
        "ZERO",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
    ]

    x = sort_str(S)

    xs = []
    for i in xrange(len(nums)):
        xs += [i] * min(x.count(c) for c in nums[i])

    for ys in ps(xs):
        S_ = ''.join(map(lambda r: nums[r], ys))
        if len(''.join(S_)) == len(x) and sort_str(S_) == x:
            # extra sort probably redundant, i'll revise later if ineff.
            return ''.join(map(str, sort(ys)))

T = int(raw_input())
for i in xrange(T):
    print 'Case #%d: %s' % (i+1, decode(raw_input()))
