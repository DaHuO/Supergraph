import sys

# sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdin = open('A-large.in', 'r')
# sys.stdout = open('a-small.out', 'w')
sys.stdout = open('a-large.out', 'w')


def solution(w):
    if len(w) < 2:
        return w
    res = w[0]
    for s in w[1:]:
        t1 = s + res
        t2 = res + s
        if t1 > t2:
            res = t1
        else:
            res = t2
    return res

for t in range(int(input())):
    r = solution(raw_input())
    print 'Case #%d: %s' % (t + 1, r)
