import itertools
TESTCASE = int(input())

def sim(hs):
    r = hs[:]
    nr = []
    while len(r) + len(nr) > 1:
        a = r.pop()
        b = r.pop()
        if a == b:
            return False
        if (['P','R','S'].index(a) - ['P','R','S'].index(b) + 3)%3 == 1:
            nr.append(a)
        else:
            nr.append(b)
        if len(r) == 0:
            r=nr[:]
            nr = []
    return True


for test in range(TESTCASE):
    n,r,p,s = map(int, input().split())
    hs = []
    cand = []
    for i in range(p):
        hs.append('P')
    for i in range(r):
        hs.append('R')
    for i in range(s):
        hs.append('S')
    ans = 'IMPOSSIBLE'
    for h in itertools.permutations(hs,2**n):
        for i in range(n):
            if sim(list(h)):
                cand.append(''.join(h))
    if cand:
        cand.sort()
        ans = cand[0]

    print('Case #' + str(test + 1) + ':', ans)
