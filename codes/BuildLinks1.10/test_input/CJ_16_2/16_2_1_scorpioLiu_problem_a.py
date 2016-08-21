import sys

sys.stdin = open('A-small-attempt1.in', 'r')
# sys.stdin = open('A-large.in', 'r')
sys.stdout = open('a-small.out', 'w')
# sys.stdout = open('a-large.out', 'w')

a = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
def solution(w):
    res = []
    w = list(w)
    w.sort()
    w = ''.join(w)
    d = dict()
    for c in w:
        d[c] = w.count(c)
    import itertools
    for i in range(1, len(w)/3 + 1):
        for k in list(itertools.product([0,1,2,3,4, 5, 6, 7, 8, 9],repeat=i)):
            r = []
            for n in k:
                r =  r + list(a[n])
            r.sort()
            if ''.join(r) == w:
                k = list(k)
                k.sort()
                return ''.join([str(i) for i in k])
    return ''.join(res)

b = []
for i, v in enumerate(a):
    d = dict()
    for c in v:
        d[c] = v.count(c)
    b.append([i, d, len(v)])
for t in range(int(input())):
    r = solution(raw_input())
    print 'Case #%d: %s' % (t + 1, r)
