def findMaxIdx(p):
    m = max(p)
    mList = [i for i, j in enumerate(p) if j == m]
    return mList

def addStep(step, mList, p, cnt, same):
    s = ""
    c = 0

    for i in mList:
        if c == cnt:
            break
        s += (chr(ord('A') + i))
        p[i] -= 1
        c += 1

    if same == 0:
        step.append(s)
    else:
        step[-1] += s

    return

def solveStep(step, n, p, cnt):
    #mList = findMaxIdx(p)
    m = max(p)
    mList = [i for i, j in enumerate(p) if j == m]

    if len(mList) - cnt == 1:
        mList = mList[0:1]
        addStep(step, mList, p, 1, 0)
        return

    addStep(step, mList, p, cnt, 0)
    cnt -= len(mList)
    #print "1", p, cnt, step
    if max(p) != 0 and cnt > 0:
        mList = findMaxIdx(p)
        addStep(step, mList, p, cnt, 1)
    #print "2", p, cnt, step
    return

def solve(n, p, cnt):
    step = []

    while max(p) != 0:
        solveStep(step, n, p, cnt)

    return step

T=int(raw_input())
for cas in xrange(1,T+1):
    N=int(raw_input())
    P=map(int,raw_input().split())
    print "Case #{}: {}".format(cas," ".join(solve(N, P, 2)))





