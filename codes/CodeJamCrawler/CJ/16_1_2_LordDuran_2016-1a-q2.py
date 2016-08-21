# from __future__ import division
from pprint import pprint
import time
inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

def recurse(lists, mat, I, J, used=False):
    if len(lists) == 0:
        return True

    N = len(lists[0])
    if I == N or J == N:
        rows_and_cols = []
        for i in xrange(N):
            #rows
            l = [mat[i][j] for j in xrange(N)]
            rows_and_cols.append(l)
        for j in xrange(N):
            #columns
            l = [mat[i][j] for i in xrange(N)]
            rows_and_cols.append(l)
        for l in lists:
            if l not in rows_and_cols:
                return False
        return True
    # Assume up to row I and col J are filled
    possible_rows = []
    possible_cols = []
    for l in lists:
        can_row = can_col = True
        if I < N:
            for j in xrange(J):
                if l[j] != mat[I][j]:
                    can_row = False
        if I > 0:
            for j in xrange(J, N):
                if l[j] <= mat[I-1][j]:
                    can_row = False
        if J < N:
            for i in xrange(I):
                if l[i] != mat[i][J]:
                    can_col = False
        if J > 0:
            for i in xrange(I, N):
                if l[i] <= mat[i][J-1]:
                    can_col = False
        if can_col:
            possible_cols.append(l)
        if can_row:
            possible_rows.append(l)

    # print 'I,J', I,J
    # print 'possible_cols', possible_cols
    # print 'possible_rows', possible_rows
    # print 'mat'
    # for l in mat:
    #     print l
    if len(possible_cols) == 0 and J < N:
        # if J >= 1:
        #     for i in xrange(N):
        #         mat[i][J] = mat[i][J-1]
        used = True
    if len(possible_rows) == 0 and I < N:
        # if I >= 1:
        #     for j in xrange(N):
        #         mat[I][j] = mat[I-1][j]
        used = True

    possible_cols.sort()
    possible_rows.sort()

    for pc in possible_cols:
        # print 'trying', pc, 'as column', J
        for i in xrange(N):
            mat[i][J] = pc[i]
        lists.remove(pc)
        if recurse(lists, mat, I, J+1):
            return True

        lists.append(pc)
    for pr in possible_rows:
        # print 'trying', pr, 'as row', I
        for j in xrange(N):
            mat[I][j] = pr[j]
        lists.remove(pr)
        if recurse(lists, mat, I+1, J):
            return True
        lists.append(pr)
    return False

def do_case(ncase):
    N, = parse_line()
    lists_copy = []
    lists = []
    for i in xrange(2*N-1):
        lists.append(parse_line())
        lists_copy.append(lists[-1][:])
    mat = [[0]*N for i in xrange(N)]

    print lists

    assert recurse(lists, mat, 0, 0, False)

    l = []
    rows_and_cols = []
    for i in xrange(N):
        #rows
        l = [mat[i][j] for j in xrange(N)]
        rows_and_cols.append(l)
    for j in xrange(N):
        #columns
        l = [mat[i][j] for i in xrange(N)]
        rows_and_cols.append(l)

    print 'mat'
    for l in mat:
        print l
    print
    print 'rnc', rows_and_cols
    print 'lc', lists_copy
    for l in lists_copy:
        rows_and_cols.remove(l)

    assert len(rows_and_cols)==1
    missing_l = rows_and_cols[0]
    
    print 'missing', missing_l

    print >>outputfile, out_s % (ncase, str(' '.join([str(c) for c in missing_l])))

start_time = time.time()
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    print "Doing case", ncase
    do_case(ncase)
    print "Done, time", time.time()-start_time
    