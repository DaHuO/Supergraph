#!/usr/bin/python2
import sys

sys.setrecursionlimit(30000)

TEST = list('--+-')
DBG = False

def flip(st, m):
    st = st[:]
    for x in range(m):
        if st[x] == '+':
            st[x] = '-'
        else:
            st[x] = '+'
    return st

def pancake(args):
    st, n, m, mat, p = args
    log("\n" + " " * n, (st, n, m))
    # print (n)
    # raw_input()
    l = len(st)
    finish = '+' * l
    sts = ''.join(st)
    obvious = '-' * l
    if sts == finish:
        if mat[finish][0] > n:
            mat[finish][0] = n
            mat[finish][1] = p
    elif sts == obvious:
        if mat[finish][0] > n + 1:
            mat[finish][0] = n + 1
            mat[finish][1] = sts
    else:
        for y in range(1, l + 1):
            tmp = flip(st, y)
            s = ''.join(tmp)
            if s in mat:
                if mat[s][0] > n + 1:
                    mat[s][0] = n + 1
                    mat[s][1] = sts
                continue
            else:
                mat[s] = [n + 1, sts]
                pancake((tmp, n + 1, y, mat, sts))

def log(*args):
    if DBG:
        print(args)

def testcase(x, s):
    # log(TEST)
    # log("''''''''''''''''''''''''''''''''''''''''")
    # log(flip(TEST, 0))
    # log(flip(TEST, 1))
    # log(flip(TEST, 2))
    # log(flip(TEST, 3))
    # log(flip(TEST, 4))
    sol = '+' * len(s)
    mat = {sol: [float('inf'), None], ''.join(s): [0, None]}
    log(pancake((s, 0, 0, mat, None)))
    log(mat)
    c = sol
    n = 0
    while mat[c][1] is not None:
        n += 1
        log(mat[c], n)
        c = mat[c][1]

    print "Case #%s: %s" % (x, n)

def main():
    inp = sys.stdin.readlines()
    log (inp)
    T = int(inp[0])
    for t in range(1, T + 1):
        testcase(t, list(inp[t].strip()))


if __name__ == '__main__':
    main()