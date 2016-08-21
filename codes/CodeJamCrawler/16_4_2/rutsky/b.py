# B
import sys
import itertools

#sys.stdin = open("small.in", "rt")
#sys.stdout = open("small.out", "wt")
#sys.stdin = open("B-small-attempt0.in", "rt")
#sys.stdout = open("B-small-attempt0.out", "wt")
sys.stdin = open("B-small-attempt1.in", "rt")
sys.stdout = open("B-small-attempt1.out", "wt")
#sys.stdin = open("B-large.in", "rt")
#sys.stdout = open("B-large.out", "wt")


def calc_probs(P):
    probs = [[0 for j in range(len(P) + 1)] for i in range(len(P))]
    probs[0][0] = 1 - P[0]
    probs[0][1] = P[0]
    for l in range(1, len(P)):
        probs[l][0] = (1 - P[l]) * probs[l - 1][0]
        for n in range(1, len(P) + 1):
            probs[l][n] = (1 - P[l]) * probs[l - 1][n] + P[l] * probs[l - 1][n - 1]

    return probs


def solve(N, K, P):
    max_prob = 0
    for comb in itertools.combinations(P, K):
        probs = calc_probs(comb)
        prob = probs[K - 1][K // 2]
        max_prob = max(prob, max_prob)

    #return "{:.12f}".format(max_prob)
    return max_prob

#for i in range(100):
#    solve(16, 8, [0.5] * 16)

#solve(16, 8, [0.5] * 16)
#1 / 0

cases = int(input())
for case_idx in range(cases):
    N, K = list(map(int, input().split()))
    P = list(map(float, input().split()))
    print("Case #{}: {}".format(case_idx + 1, solve(N, K, P)))
