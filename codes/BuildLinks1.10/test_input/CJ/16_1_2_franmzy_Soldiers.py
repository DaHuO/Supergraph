# -*- coding: utf-8 -*-
######################################################
##                                                  ##
##  Fran Muñoz                                      ##
##  email: fran.mzy@gmail.com                       ##
##  UVA user: franmzy                               ##
##  Linkedin: https://www.linkedin.com/in/franmzy   ##
##                                                  ##
######################################################

l = [None]*55*2
field = [[None for i in range(60)] for i in range(60)]

rowIns = [False] * 55
colIns = [False] * 55


def insertRow (n, row):
    for j in range(N):
        if(rowIns[n] or (field[n][j] and field[n][j] != row[j])):
            return False
    field[n] = row[:]
    rowIns[n] = True
    return True

def insertCol (n, col):
    for i in range(N):
        if(colIns[n] or (field[i][n] and field[i][n] != col[i])):
            return False
    for i in range(N):
        field[i][n] = col[i]
    colIns[n] = True
    return True

def deleteRow (n):
    for j in range(N):
        if not colIns[j]:
            field[n][j] = None
    rowIns[n] = False

def deleteCol (n):
    for i in range(N):
        if not rowIns[i]:
            field[i][n] = None
    colIns[n] = False


def backtracking(n):

    if n == N*2-1:
        return True

    # i = l[0].index(l[n][0]) if l[n][0] in l[0] else None
    # if i :
    for i in range(N):
        if insertRow(i, l[n]):
            if backtracking(n+1):
                return True
            deleteRow(i)

    # j = l[1].index(l[n][0]) if l[n][0] in l[1] else None
    # if j :

        if insertCol(i, l[n]):
            if backtracking(n+1):
                return True
            deleteCol(i)

    return False





n_cases = int(input())

for i_case in range(n_cases):

    N = int(input())

    l = [None]*(N*2-1)
    field = [[None for i in range(60)] for i in range(60)]

    rowIns = [False] * N
    colIns = [False] * N

    for i in range(N*2-1):
        l[i] = list(map(int, input().split()))

    l.sort();

    # insertRow(0, l[0])
    # insertCol(0, l[1])


    backtracking(0)

    # for i in range(N):
    #     print(field[i][:N])
    # print()

    # print(rowIns, colIns)

    i = rowIns.index(False) if False in rowIns else None
    if i != None:
        print('Case #{0}: {1}'.format(i_case+1, ' '.join(map(str,(field[i][:N])))))

    j = colIns.index(False) if False in colIns else None
    if j != None:
        print('Case #{0}: {1}'.format(i_case+1, ' '.join(map(str,[field[i][j] for i in range(N)]))))



