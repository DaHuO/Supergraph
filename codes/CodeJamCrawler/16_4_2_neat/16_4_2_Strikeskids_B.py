#!/usr/bin/env python3

def compute_prob_list(probs):
    if len(probs) % 2 == 1: return 0.0
    dp = [1.0] + [0.0]*len(probs)
    for p in probs:
        for i in range(len(probs)-1, 0, -1):
            dp[i] = dp[i] * (1-p) + dp[i-1] * p
        dp[0] = dp[0] * (1-p)

    return dp[len(probs)//2]

def compute_prob_slow(N, K):
    probs = sorted(map(float, input().split()))

    from itertools import combinations

    best = 0

    for c in combinations(probs, K):
        b = compute_prob_list(c)
        if b > best:
            best = b
    return best

def run_test(i):
    nums = map(int, input().split())
    print('Case #%d: %s' % (i, compute_prob_slow(*nums)))

def main():
    T = int(input())

    for t in range(T):
        run_test(t+1)

def extensive():
    import random
    for i in range(100000):
        compute_insomnia(random.randint(0, 10**6))
    exit(0)

if __name__ == '__main__': main()