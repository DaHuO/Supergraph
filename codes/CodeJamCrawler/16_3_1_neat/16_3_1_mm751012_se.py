import sys

rl = lambda: sys.stdin.readline().strip()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def senate(Ps, out, i):
    #print 'senate',alpha[i]
    Ps[i] -= 1
    out.append(alpha[i])
    return Ps, out

def senate2(Ps, out, i, j):
    #print 'senate',alpha[i],alpha[j]
    Ps[i] -= 1
    Ps[j] -= 1
    out.append(alpha[i]+alpha[j])
    return Ps, out

def check(Ps):
    sumP = sum(Ps)
    for P in Ps:
        if P>(sumP/2):
            print '*****error', Ps, sumP/2
            exit();

for case in range(int(rl())):
    N = int(rl())
    Ps = map(int, rl().split())
    #print Ps

    Pdict = dict(zip(range(N), Ps))
    Pdict_sorted = sorted(Pdict.items(), key=lambda x:x[1], reverse=True)
    #print Pdict

    out = []

    # if not even, cut to even minP
    minP = min(Ps)
    while min(Ps)!=max(Ps):
        Pdict = dict(zip(range(N), Ps))
        Pdict_sorted = sorted(Pdict.items(), key=lambda x: x[1], reverse=True)
        Ps, out = senate(Ps, out, int(Pdict_sorted[0][0]))
        #print 'to even', Ps, out
        check(Ps)

    # now even
    # if only ABs, cut ABs to empty
    if N==2:
        for i in range(Ps[0]):
            Ps, out = senate2(Ps, out, 0, 1)
            #print 'to even', Ps, out
            check(Ps)
    # cut to all 1s, if minP=1
    elif minP==1:
        for i in range(minP - 1):
            for j in range(N):
                Ps, out = senate(Ps, out, j)
                #print 'to 1s', Ps, out
                check(Ps)
        # now all 1s
        # cut to AB
        for i in range(2, N):
            Ps, out = senate(Ps, out, i)
            #print 'to AB', Ps, out
            check(Ps)
        # now AB
        Ps, out = senate2(Ps, out, 0, 1)
        #print 'to empty', Ps, out

    # cut to all 2s, if minP>1
    else:
        for i in range(minP - 2):
            for j in range(N):
                Ps, out = senate(Ps, out, j)
                #print 'to 2s', Ps, out
                check(Ps)
        # now all 2s
        # cut to AABB
        for i in range(2, N):
            Ps, out = senate2(Ps, out, i, i)
            #print 'to AABB', Ps, out
            check(Ps)
        # now AABB
        Ps, out = senate2(Ps, out, 0, 1)
        Ps, out = senate2(Ps, out, 0, 1)
        #print 'to empty', Ps, out

    # output
    print 'Case #' + str(case + 1) + ':', ' '.join(out)

