
import csv
import itertools
import copy
import time
import numpy as np
import copy


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        N = int(csv_r.next()[0])
        test=[]
        for _ in range(2*N-1):
            test.append([int(e) for e in csv_r.next()])
        test_lst.append(test)
    f.close() 
    return test_lst 


def check():
    #d={'C': {0: [1, 2, 3], 1: [2, 3, 4], 2: [3, 5, 6]}, 'R': {}, 'U': [[1, 2, 3], [2, 3, 5]], 'N': 3}
    d={'C': {}, 'R': {0: [1, 2, 3]}, 'U': [[1, 2, 3], [2, 3, 5], [3, 5, 6], [2, 3, 4]], 'N': 3}

    #d={'N': 3, 'R':{0:[1,2,3], 1:[2,3,4], 2:[3,5,6]}, 'C':{0:[1,2,3], 1:[2,3,5]}, 'U':[]}
    print is_ok(d)


def is_ok(d):
    t=[] 
    N=d['N']
    for i in xrange(N):
        if i in d['R']:
            t.append(d['R'][i])
        else:
            t.append([None]*N)
    for i in xrange(N):
        if i in d['C']:
            c=d['C'][i]
            is_ok = True
            for i_e, e in enumerate(c):
                if t[i_e][i] is not None and t[i_e][i]!=e:
                    return False
                if t[i_e][i] is None:
                    t[i_e][i]=e
    #
    for i in xrange(N):
        row=[e for e in t[i] if e is not None]
        s_row=row[:]
        s_row.sort() 
        if len(row) > 0 and row != s_row:
            return False
    for i in xrange(N):
        col=[e[i] for e in t if e[i] is not None]
        s_col=col[:]
        s_col.sort() 
        if len(col) > 0 and col != s_col:
            return False
    return True


def extract_sol(d):
    t=[] 
    N=d['N']
    for i in xrange(N):
        if i in d['R']:
            t.append(d['R'][i])
        else:
            t.append([None]*N)
    for i in xrange(N):
        if i in d['C']:
            c=d['C'][i]
            is_ok = True
            for i_e, e in enumerate(c):
                if t[i_e][i] is None :
                    t[i_e][i]=e
    for i in xrange(N):
        if i not in d['R']:
            return t[i]
        if i not in d['C']:
            return [e[i] for e in t]
 

def process(d):
    if len(d['U'])== 0:
        return extract_sol(d)
    else:
        l=d['U'].pop()
        for i in xrange(d['N']):
            d1=copy.deepcopy(d)
            if i not in d1['R']:
                d1['R'][i]=l
                if is_ok(d1):
                    res=process(d1)
                    if res is not None:
                        return res 
            d2=copy.deepcopy(d)
            if i not in d2['C']:
                d2['C'][i]=l
                if is_ok(d2):
                    res=process(d2)
                    if res is not None:
                        return res 


def solve_test(test_case):
    N=(len(test_case)+1)/2
    res=process({'N':N, 'U':test_case, 'R' : {}, 'C' : {}})
    return res


def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %s" % (1+i_test, ' '.join([str(e) for e in res]))


if __name__ == '__main__':
    #main('./A-large.in')
    #check()
    #main('./simple.in')
    main('./B-small-attempt1.in')
    #main('./A-small-attempt0.in')
    #main('./C-small-attempt0.in')

