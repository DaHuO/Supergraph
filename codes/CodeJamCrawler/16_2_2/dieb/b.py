import sys
import operator

def read_one_line():
  return sys.stdin.readline().rstrip()


def expand_space(start):
    candidates = [start]

    while any(['?' in c for c in candidates]):
        for cand in candidates:
            if '?' not in cand:
                continue
            else:
                candidate = candidates.pop(candidates.index(cand))

                for num in '0123456789':
                    cs = candidate.replace('?', num, 1)
                    candidates.append(cs)
                break

    return [int(c) for c in candidates]


def pad(pair, length):
    return (str(pair[0]).zfill(length), str(pair[1]).zfill(length))


def solve(C, J):
    candidates_c = expand_space(C)
    candidates_j = expand_space(J)

    diffs = {}

    for c in candidates_c:
        for j in candidates_j:
            diff = abs(c - j)
            diffs.setdefault(diff, [])
            diffs[diff].append((c, j))

    diffs_sorted = sorted(diffs.items(), key=operator.itemgetter(0))

    # Minimum diff
    best_score, best_pairs = diffs_sorted[0]

    # Minimum C score
    best_pairs = sorted(best_pairs, key=operator.itemgetter(0))
    pairs_with_same_best_c = []
    c = best_pairs[0][0]

    for pair in best_pairs:
        if pair[0] == c:
            pairs_with_same_best_c.append(pair)
        else:
            break

    best_pairs = pairs_with_same_best_c

    # Minimum J score
    best_pairs = sorted(best_pairs, key=operator.itemgetter(1))

    return pad(best_pairs[0], len(C))


if __name__ == '__main__':
  num_cases = int(read_one_line())

  for case in xrange(num_cases):
    coders, jammers = solve(*read_one_line().split(' '))

    print 'Case #%d: %s %s' % (case + 1, coders, jammers)