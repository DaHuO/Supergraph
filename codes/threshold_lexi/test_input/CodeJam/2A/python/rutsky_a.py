# A
import sys
import itertools

#sys.stdin = open("small.in", "rt")
#sys.stdout = open("small.out", "wt")
sys.stdin = open("A-small-attempt0.in", "rt")
sys.stdout = open("A-small-attempt0.out", "wt")
#sys.stdin = open("A-large.in", "rt")
#sys.stdout = open("A-large.out", "wt")


class SameError(Exception):
    pass


def choose(a, b):
    if {a, b} == {'R', 'P'}:
        return 'P'
    if {a, b} == {'R', 'S'}:
        return 'R'
    if {a, b} == {'P', 'S'}:
        return 'S'
    raise SameError


def check(line):
    if len(line) == 1:
        return True
    else:
        try:
            assert len(line) % 2 == 0
            return check([choose(a, b) for a, b in zip(line[::2], line[1::2])])
        except SameError:
            return False


def solve(N, R, P, S):
    for perm in itertools.permutations('P' * P + 'R' * R + 'S' * S):
        if check(perm):
            return "".join(perm)

    return "IMPOSSIBLE"

#for i in range(25):
#    solve(3, 2, 2, 4)

cases = int(input())
for case_idx in range(cases):
    N, R, P, S = list(map(int, input().split()))
    print("Case #{}: {}".format(case_idx + 1, solve(N, R, P, S)))
