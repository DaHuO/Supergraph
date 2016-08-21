import sys

_in = open(sys.argv[1])
def raw(): return _in.readline().rstrip('\n')
def ints(): return map(int, raw().split())
raw_input = raw # we all forget sometimes

class memoize:
    def __init__(self, function):
        self.fn = function
        self.memory = {}
    def __call__(self, *args):
        if args not in self.memory:
            self.memory[args] = self.fn(*args)
        return self.memory[args]

@memoize
def rec(winner, R, P, S, k):
    # winner is 0 R, 1 P, 2 S
    assert R + P + S == 2**k
    L = [R,P,S]
    if k == 1:
        if 2 in L:
            return False
        a = L.index(1)
        b = 2 - (L[::-1].index(1))
        r = (a-b)%3
        if r == 1:
            win = a
        else:
            assert r == 2
            win = b
        return winner == win
    loser = (winner-1)%3
    best_pair = ("Z", None)
    for p in range(P, -1, -1):
        for r in range(R, -1, -1):
            s = 2**(k-1) - r - p
            if s < 0 or s > S:
                continue
            left = (winner, r, p, s, k-1)
            right = (loser, R-r, P-p, S-s, k-1)
            if rec(*left) and rec(*right):
                sol = solution(*left) + solution(*right)
                best_pair = min(best_pair, (sol, (left, right)))
            left = (loser, r, p, s, k-1)
            right = (winner, R-r, P-p, S-s, k-1)
            if rec(*left) and rec(*right):
                sol = solution(*left) + solution(*right)
                best_pair = min(best_pair, (sol, (left, right)))
    if best_pair[0] != "Z":
        return best_pair[1]
    return None

def solution(winner, R, P, S, k):
    if k == 1:
        return "P"*P + "R"*R + "S"*S
    left, right = rec(winner, R, P, S, k)
    return solution(*left) + solution(*right)

def solve(N, R, P, S):
    for i in range(3):
        if rec(i, R, P, S, N):
            return solution(i, R, P, S, N)
    return "IMPOSSIBLE"

if __name__ == '__main__':
    num_cases, = ints()
    for case_num in xrange(1, num_cases + 1):
        N, R, P, S = ints()
        print "Case #{}: {}".format(case_num, solve(N, R, P, S))
