import string
import sys

import collections

fin = sys.stdin
num_cases = int(fin.readline().strip())


def solve(counts):
    solution = ""
    counter = collections.Counter()
    total = 0
    for letter, count in zip(list(string.ascii_uppercase), counts):
        counter[letter] = count
        total += count

    while total > 3:
        letters = [k for k,c in counter.most_common(2)]
        solution = "{} {}".format(solution, "".join(letters))
        for l in letters:
            counter[l] -= 1
        total -= 2

    if total == 3:
        letters = [k for k,c in counter.most_common(1)]
        solution = "{} {}".format(solution, "".join(letters))
        for l in letters:
            counter[l] -= 1
        total -= 1

    letters = [k for k, c in counter.most_common(2)]
    solution = "{} {}".format(solution, "".join(letters))

    return solution

for t in range(num_cases):
    N = int(fin.readline().strip())
    counts = [int(a) for a in fin.readline().strip().split()]

    print("Case #{}: {}".format(t + 1, solve(counts)))
