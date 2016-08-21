import sys


def f(winner, n):
    #print n, winner
    if n == 0:
        if winner == 0:
            return 'R'
        elif winner == 1:
            return 'P'
        elif winner == 2:
            return 'S'
    else:
        a = f(winner, n-1)
        b = f((winner-1) % 3, n-1)
        if a < b:
            return a + b
        else:
            return b + a


def solve(N, R, P, S):
    n, r, p, s = N, R, P, S
    winner = None
    while True:
        if n == 0:
            if r == 1:
                winner = 0
            elif p == 1:
                winner = 1
            elif s == 1:
                winner = 2
            else:
                assert False
            break
        elif n == 1:
            if r >= 2 or p >= 2 or s >= 2:
                return 'IMPOSSIBLE'
            else:
                if r == 0:
                    winner = 2
                elif p == 0:
                    winner = 0
                elif s == 0:
                    winner = 1
                else:
                    assert False
                break
        else:
            r -= 2 ** (n - 2)
            p -= 2 ** (n - 2)
            s -= 2 ** (n - 2)
            n -= 2
            if r < 0 or p < 0 or s < 0:
                return 'IMPOSSIBLE'
            r, p, s = s, r, p

    return f(winner, N)


T = int(sys.stdin.readline())
for i in range(T):
    N, R, P, S = map(int, sys.stdin.readline().split())

    print "Case #{}:".format(i+1),
    print solve(N, R, P, S)

