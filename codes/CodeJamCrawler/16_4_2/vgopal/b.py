from collections import defaultdict
from itertools import combinations

FILENAME = 'b-large.txt'

f = open(FILENAME)

def probability_of_tie(probabilities):
    sums = defaultdict(lambda: 0)
    count = 0
    for p in probabilities:
        count += 1
        if not sums:
            sums[0] = 1 - p
            sums[1] = p
            continue
        # print sums, count
        for i in xrange(count, 0, -1):
            # print 'setting', i, i - 1
            sums[i] = sums[i] + sums[i - 1] * p
            sums[i-1] *= (1 - p)
    # print sums
    return sums[len(probabilities) / 2]

def answer(N, K, probabilities):
    probabilities = sorted(probabilities)
    best = -1
    best_combo = None
    for combination in combinations(probabilities, K):
        p = probability_of_tie(combination)
        if p > best:
            best = p
            best_combo = sorted(combination)
            # print best, combination
    indices = []
    start = 0
    for p in best_combo:
        if probabilities[start] == p:
            start += 1
        else:
            indices.append(start)
            start = probabilities.index(p) + 1

    # for x in xrange(0, len(probabilities)):
    #     for y in xrange(x, len(probabilities) + 1):
    #         if best_combo == (probabilities[:x] + probabilities[y:]):
    #             return
    # print "NOPE"
    # # if best_combo == probabilities[:K] or best_combo == probabilities[K:]
    # # if len(indices) == 2 and best_combo[0] == probabilities[0] and best_combo[-1] == probabilities[-1]:
    # print '-----------------'
    # print probabilities
    # print best_combo
    # print indices
    # for i in xrange(2, K, 2):
    #     _, combo = answer(N, i, probabilities)
    #     for x in combo:
    #         if x not in best_combo and i <= 4:
    #             print 'NOPE', len([x for x in best_combo if x < 0.5]) == K / 2 or best_combo == probabilities[-K:], sorted(combo), sorted(best_combo), N, K, probabilities
    return best, sorted(best_combo)

def long_answer(N, K, probabilities):
    probabilities = sorted(probabilities)
    best = -1
    best_combo = None
    for x in xrange(K + 1):
        y = N - (K - x)
        combo = probabilities[:x] + probabilities[y:]
        # print N, K, x, y
        assert len(combo) == K
        p = probability_of_tie(combo)
        if p > best:
            best = p
            best_combo = combo
    return best


num_cases = int(f.readline())
for case in xrange(1, num_cases + 1):
    N, K = [int(x) for x in f.readline().split()]
    probabilities = [float(x) for x in f.readline().split()]
    # val, _ = answer(N, K, probabilities)
    val = long_answer(N, K, probabilities)
    # old_val = answer(N, K, probabilities)
    # if abs(val - long_answer(N, K, probabilities)) > 0.000001:
    #     raise 'NO'
    # if abs(val - long_answer(N, K, probabilities)) > 0.000001:
    #     # if not (0 in probabilities or 1 in probabilities):
    #     print case, N, K, probabilities, val, long_answer(N, K, probabilities)
    print 'Case #{}: {}'.format(case, val)
