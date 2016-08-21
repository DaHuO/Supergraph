from collections import Counter

n_counts = map(Counter, ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"))
DP = {}
def solve(counter):
    if frozenset(counter.items()) in DP:
        return DP[frozenset(counter.items())]

    if not counter:
        return []

    for i, count in enumerate(n_counts):
        if all(counter[k] - v >= 0 for k, v in count.items()):
            #print counter - count
            solution = solve(counter - count)
            DP[frozenset((counter - count).items())] = solution
            if solution is not None:
                return [i] + solution
            

T = int(raw_input())

for case in xrange(1, T + 1):
    numbers = solve(Counter(raw_input()))
    print 'Case #{}: {}'.format(case, ''.join(map(str, numbers)))
