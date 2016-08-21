import sys
from collections import deque

def find_plan(parties):
    plan = []
    x = parties
    while True:
        # print x
        if sum(x) == 0:
            return plan
        r = sorted(range(len(x)), key=lambda i: x[i], reverse=True)
        first, second = r[0], r[1]
        if sum(x) % 2:
            x[first] -= 1
            plan.append((first,))
        elif x[first] >= x[second] + 2:
            x[first] -= 2
            plan.append((first,) * 2)
        else:
            x[first] -= 1
            x[second] -= 1
            plan.append((first, second))
        assert(all(p <= sum(x) / 2 for p in x)), "%d: %s" % (sum(x), str(x))
    raise Exception("no solution")


def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        N = int(sys.stdin.readline())
        P = map(int, sys.stdin.readline().split())
        parties = [0] * 26
        for i in range(len(P)):
            parties[i] = P[i]
        plan = find_plan(parties)
        output = ["".join(map(lambda c: chr(c + ord('A')), p)) for p in plan]
        print "Case #%d:" % t, " ".join(output)

if __name__ == "__main__":
    main()
