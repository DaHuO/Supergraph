import itertools


def probability(k, current):
    sum = 0
    for comb in itertools.combinations(range(len(current)), k / 2):
        internal = 1
        for i, value in enumerate(current):
            if i in comb:
                internal *= value
            else:
                internal *= 1 - value
        sum += internal
    return sum


def solve(n, k, data):
    result = 0
    for comb in itertools.combinations(data, k):
        result = max(result, probability(k, comb))
    return result


def main():
    with open("B-input.in") as fin:
        with open("B-output.out", 'w') as fout:
            num_t = int(fin.readline())
            for t in xrange(num_t):
                n, k = map(int, fin.readline().strip().split())
                data = map(float, fin.readline().strip().split())
                fout.write("Case #%d: %f\n" % (t + 1, solve(n, k, data)))


main()
