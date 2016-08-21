import sys

# sys.stdin = open('B-small-attempt0.in', 'r')
sys.stdin = open('B-large.in', 'r')
# sys.stdin = open('B-sample.in', 'r')


# sys.stdout = open('B-large.out', 'w')


def solve(A):
    # print('A', A)

    N = len(A)
    L = [1]
    for i in range(N):
        p = A[i]
        X = [0] * (i + 2)
        # j = i
        # while j >= 0:
        #     L[j + 1] += L[j] * p
        #     L[j] += L[j] * (1 - p)
        #     j -= 1
        for j in range(i + 1):
            X[j + 1] += L[j] * p
            X[j] += L[j] * (1 - p)
        L = X
    return L[N // 2]


def gao():
    for t in range(1, int(input()) + 1):

        _N, K = map(int, input().split())
        P = sorted(map(float, input().split()))

        result = 0

        for beg in range(_N - K + 1):
            result = max(result, solve([P[p] for p in range(_N) if p in range(beg, beg + K)]))

        for beg in range(K + 1):
            result = max(result, solve([P[p] for p in range(_N) if p not in range(beg, beg + _N - K)]))

        print('Case #%s: %.6f' % (t, result))


gao()
