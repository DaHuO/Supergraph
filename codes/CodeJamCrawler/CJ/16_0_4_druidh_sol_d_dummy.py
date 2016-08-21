#!/usr/bin/python2.7
import itertools

def Evoluciona(cur_mat, ini):
    mat = []
    for i in cur_mat:
        if (i==1):
            mat.extend([1]*len(ini))
        else:
            mat.extend(ini)
    return mat

def SumCol(mat):
    col_sum = []
    for j in xrange(len(mat[0])):
        temp = 0
        for i in xrange(len(mat)):
            temp+=mat[i][j]
        col_sum.append(temp)
    return col_sum

for case in range(input()):
    K, C, S = map(int, raw_input().split())
    sol = [i+1 for i in xrange(S)]
    """
    combi = 2**K
    sol = []

    mat_ini = []
    mat = []
    for p in itertools.product((0,1), repeat=K):
        mat.append(list(p))
        mat_ini.append(list(p))

    for i in xrange(C-1):
        col_sum = SumCol(mat)
        if (max(col_sum) == (combi-1)):
            sol.append(col_sum.index(max(col_sum)) + 1)
            break
        else:
            for i in xrange(len(mat)):
                mat[i] = Evoluciona(mat[i], mat_ini[i])

#    print mat
    solPrinted = False
    if (len(sol) == 0):
        while (S > 0):
            col_sum = SumCol(mat)
            ind = col_sum.index(max(col_sum))
            sol.append(ind+1)
            new_mat = []
            for row in mat:
                if (row[ind] == 0):
                    new_mat.append(row)
            mat = new_mat[:]
            S = S-1
            if (len(mat) == 1):
                break
        if (len(mat) > 1):
            solPrinted = True
            print 'Case #%s: IMPOSSIBLE' % (case + 1)

    if (not solPrinted):
        if (len(sol) > 0):
            print 'Case #%s: %s' % ((case + 1), ' '.join(map(str, sol)))
        else:
            print 'Case #%s: IMPOSSIBLE' % (case + 1)
    """            
    print 'Case #%s: %s' % ((case + 1), ' '.join(map(str, sol)))

