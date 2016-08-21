## Problem B
import collections
from copy import deepcopy as dc

def fillgridrow(grid, vec, ind):
    if grid == None:
        return grid
    for i in range(0, len(grid)):
        if grid[i][ind] == vec[ind]:
            for j in range(0, len(grid)):
                if grid[i][j] != 0 and vec[j] != grid[i][j]: return None
                grid[i][j] = vec[j]
            return grid
    return None

def fillgridcol(grid, vec, ind):
    if grid == None:
        return grid
    for i in range(0, len(grid)):
        if grid[ind][i] == vec[ind]:
            for j in range(0, len(grid)):
                if grid[j][i] != 0 and vec[j] != grid[j][i]: return None
                grid[j][i] = vec[j]
            return grid
    return None

def recSolve(grid, m, rm, mlist, rlist):
    #print(grid)
    #print(mlist)
    #print(rlist)
    #print('')
    if grid == None:
        return grid
    N = len(grid)
    if len(mlist) > 0:
        choice = mlist[0]
        # try as row
        gr = dc(grid)
        gr = fillgridrow(gr, m[choice][0], 0)
        if len(m[choice]) > 1:
            gr = fillgridcol(gr, m[choice][1], 0)
        if gr == None:
            res = None
        else:
            res = recSolve(gr, m, rm, mlist[1:], rlist)
        if res != None:
            return res
        # try as col
        gr = dc(grid)
        gr = fillgridcol(gr, m[choice][0], 0)
        if len(m[choice]) > 1:
            gr = fillgridrow(gr, m[choice][1], 0)
        if gr == None:
            res = None
        else:
            res = recSolve(gr, m, rm, mlist[1:], rlist)
        if res != None:
            return res
    if len(rlist) > 0:
        choice = rlist[0]
        # try as row
        gr = dc(grid)
        gr = fillgridrow(gr, rm[choice][0], N-1)
        if len(rm[choice]) > 1:
            gr = fillgridcol(gr, rm[choice][1], N-1)
        if gr == None:
            res = None
        else:
            res = recSolve(gr, m, rm, mlist, rlist[1:])
        if res != None:
            return res
        # try as col
        gr = dc(grid)
        gr = fillgridcol(gr, rm[choice][0], N-1)
        if len(rm[choice]) > 1:
            gr = fillgridrow(gr, rm[choice][1], N-1)
        if gr == None:
            res = None
        else:
            res = recSolve(gr, m, rm, mlist, rlist[1:])
        if res != None:
            return res
    if len(mlist) == 0 and len(rlist) == 0:
        return grid
    return None

def probB(N, lines, revlines):
    grid = [[]] * N
    for i in range(0, N):
        grid[i] = [0]*N
    lines.sort()
    revlines.sort()
    revlines.reverse()

    matches = collections.defaultdict(list)
    revmatches = collections.defaultdict(list)
    pos = collections.Counter()
    rpos = collections.Counter()

    ## Step 1: identify one corner
    if lines[0][0] == lines[1][0]:
        grid[0] = lines[0]
        for i in range(0, N):
            grid[i][0] = lines[1][i]
        pos.update(lines[0])
        pos.update(lines[1])
        for i in range(2, len(lines)):
            matches[lines[i][0]].append(lines[i])
            revmatches[lines[i][N-1]].append(lines[i])
    else:
        for i in range(0, len(revlines)):
            revlines[i].reverse()
        grid[-1] = revlines[0]
        for i in range(0, N):
            grid[i][-1] = revlines[1][i]
        rpos.update(revlines[0])
        rpos.update(revlines[1])
        for i in range(2, len(revlines)):
            matches[revlines[i][0]].append(revlines[i])
            revmatches[revlines[i][N-1]].append(revlines[i])

    ## Step 2: identify possible matches, swaps
    torem = []
    for m in matches:
        if len(matches[m]) == 1 and pos[m] == 1:
            res = fillgridrow(grid, matches[m][0], 0)
            if res == None:
                res = fillgridcol(grid, matches[m][0], 0)
            if res != None:
                grid = res
            torem.append(m)
    for v in torem:
        del matches[v]
    torem = []
    for m in revmatches:
        if len(revmatches[m]) == 1 and rpos[m] == 1:
            res = fillgridrow(grid, revmatches[m][0], N-1)
            if res == None:
                res = fillgridcol(grid, revmatches[m][0], N-1)
            if res != None:
                grid = res
            torem.append(m)
    for v in torem:
        del revmatches[v]

    ## Step 3: search w/backtrack
    res = recSolve(grid, matches, revmatches, matches.keys(), revmatches.keys())

    ## Step 4: identify missing row/col
    lns = list()
    for i in range(0, N):
        lns.append(('%d '*N) % tuple(res[i]))
    for i in range(0, N):
        lns.append(('%d '*N) % tuple(x[i] for x in res))
    lns = collections.Counter(lns)

    for x in lines:
        tmp = (('%d '*N) % tuple(x))
        lns[tmp] = lns[tmp] - 1
        if lns[tmp] == 0:
            del lns[tmp]

    return lns.keys()[0]
    
for i in range(1, int(raw_input()) + 1):
    N = int(raw_input())
    lines, revlines = [], []
    for j in range(0, 2*N-1):
        tmp = list(int(n) for n in raw_input().split())
        revtmp = tmp[::-1]
        lines.append(tmp)
        revlines.append(revtmp)

    #print(lines)
    print "Case #%d: %s" % (i, probB(N, lines, revlines))
