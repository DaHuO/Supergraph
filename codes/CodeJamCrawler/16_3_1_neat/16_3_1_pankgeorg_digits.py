#!/usr/bin/python3

# Z=0, W=2, U=4, X=6, G=8,
# O=1, R=3, F=5, S=7

from collections import Counter

keys = []


def senate(parties):
    pts = dict([(chr(i+ord('A')), int(p)) for i, p in enumerate(input().split())])
    cnt = Counter(pts)
#    print(cnt)
    [(p1, c1), (p2, c2)] = cnt.most_common(2)
    plan = (c1-c2) * [p1]
    for (p, c) in cnt.most_common()[2:]:
        plan+= ((c//2 * [p+p])+(c-2*(c//2))*[p])

    plan = plan + c2*[p1+p2]
    return " ".join(plan)


def codejammer():
    Rounds = int(input())
    for r in range(1, Rounds + 1):
        print("Case #{}: {}".format(r, senate(input())))

if __name__ == '__main__':
    codejammer()
