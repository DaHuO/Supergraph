import sys
from copy import deepcopy
from random import randint

from collections import Counter,deque
from itertools import combinations

IS_LOCAL = False
try:
    import os
    IS_LOCAL = os.getenv("AGLAE") == "nondual" and os.getenv("SIDONIE") == "improbable"
except:
    pass

def read_ints(inp = sys.stdin):
    return list(map(int,next(inp).strip().split()))


def sol1(N, lists):

    def putcol(i, mat, col):
        for k in range(i):
            if mat[k][i] and (mat[k][i]!=col[k]):
                return False
        for k in range(N):
            if i:
                if mat[k][i-1] >= col[k]:
                    return False
            mat[k][i] = col[k]
        return True

    def putrow(i, mat, row):
        for k in range(i):
            if mat[i][k] and (mat[i][k]!=row[k]):
                return False
        for k in range(N):
            if i:
                if mat[i-1][k] >= row[k]:
                    return False
            mat[i][k] = row[k]
        return True


    def helper(i, mat, missing_row, missing_col):
        if i==N:
            if missing_row is not None:
                return mat[missing_row]
            assert missing_col is not None
            return [mat[missing_col][k] for k in range(N)]
        colbase=mat[0][i]
        colcands=[idx for idx,l in enumerate(lists) if l[0]==colbase]
        assert colcands
        backup = deepcopy(mat)
        for k,idx in enumerate(colcands):
            if putcol(i, mat, lists[idx]):
                if missing_col!=0:
                    rowbase=mat[i][0]
                    if rowbase==colbase:
                        if len(colcands)==1:
                            if missing_row is not None or missing_col is not None:
                                return None
                        if putrow(i, mat, lists[colcands[1-k]]):
                            res = helper(i+1, mat, missing_row, missing_col)

                    rowcands=[idx for idx,l in enumerate(lists) if l[0]==rowbase]
                res = helper()
            if len(colcands)>=2:
                mat = deepcopy(backup)

    def helper_col(i, mat, missing_row, missing_col, used):
        # put a col
        if i==N:
            if missing_row is not None:
                return mat[missing_row]
            assert missing_col is not None
            return [mat[k][missing_col] for k in range(N)]
        colbase=mat[0][i]
        colcands=[idx for idx,l in enumerate(lists) if l[0]==colbase and idx not in used]
        assert len(colcands)<=2
        backup = deepcopy(mat)
        for idx in colcands:
            if putcol(i, mat, lists[idx]):
                res = helper_row(i, mat, missing_row, missing_col, used | {idx})
                if res is not None:
                    return res
            mat = deepcopy(backup)
        if missing_row is not None or missing_col is not None:
            return None
        else:
            return helper_row(i, mat, None, i, used)

    def helper_row(i, mat, missing_row, missing_col, used):
        # put a row
        if missing_col == 0:
            rowbase=mat[i][1]
            rowcands=[idx for idx,l in enumerate(lists) if l[1]==rowbase and idx not in used]
        else:
            rowbase=mat[i][0]
            rowcands=[idx for idx,l in enumerate(lists) if l[0]==rowbase and idx not in used]
        assert len(rowcands)<=2
        backup = deepcopy(mat)
        for idx in rowcands:
            if putrow(i, mat, lists[idx]):
                res = helper_col(i+1, mat, missing_row, missing_col, used | {idx})
                if res is not None:
                    return res
            mat = deepcopy(backup)
        if missing_row is not None or missing_col is not None:
            return None
        else:
            return helper_col(i+1, mat, i, None, used)

    #amorce
    mini = min(l[0] for l in lists)
    cands = [idx for idx,l in enumerate(lists) if l[0]==mini]
    mat = [ [0]* N for _ in range(N)]
    putrow(0, mat, lists[cands[0]])
    if len(cands)==1:
        res = helper_col(1, mat, None, 0, {cands[0]})
    else:
        assert(len(cands)==2)
        putcol(0, mat, lists[cands[1]])
        res = helper_col(1, mat, None, None, set(cands))

    return " ".join(map(str,res))


if IS_LOCAL:
    #inp = iter(map(str,[1,3, "1 2 3", "2 3 5", "3 5 6", "2 3 4", "1 2 3"]))
    # inp = iter(map(str,[1,3, "5 7 8", "3 5 7", "5 6 8", "2 3 5", "2 4 5"]))
    # inp = iter(map(str,[1,3, "2 4 6", "2 6 8", "6 8 15", "8 12 15", "4 7 12"]))
    # inp = iter(map(str,[1,2, "2 6", "6 8", "4 8", "2 3 4", "1 2 3"]))
    # inp = open("A-small-attempt0.in")
    inp = sys.stdin
else:
    inp = sys.stdin

T ,= read_ints(inp)
# T=1
mm = 0
for t in range(T):
    N, =read_ints(inp)
    lists = []
    for _ in range(2*N-1):
        lists.append(read_ints(inp))
    # if i>=mm:
    #     print(N,i,x)
    #     mm=i
    x = sol1(N, lists)
    print("Case #%d: %s" % (t+1,x) )
