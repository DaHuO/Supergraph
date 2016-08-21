__author__ = 'jin-yc10'
import math, sys

f=file("B-large.in", 'r')
T=int(f.readline())
o=file("2.out", "w")
for i in xrange(T):
    N=int(f.readline())
    # print N
    buf=[]
    grid=[]

    r_flag=[-1 for x in xrange(N)]
    l_flag=[-1 for x in xrange(N)]

    for j in xrange(N):
        grid.append([-1 for x in xrange(N)])
    for j in xrange(2*N-1):
        l=[int(x) for x in f.readline().split()]
        buf.append(l)
    # print buf,grid

    # algo
    for j in xrange(N):
        a = [buf[x][j] for x in xrange(2*N-1)]
        m = sys.maxint
        for k in xrange(2*N-1):
            if k in l_flag or k in r_flag:
                continue
            elif buf[k][j] < m:
                m = buf[k][j]
        # print 'm =', m
        cnt = 0
        sel = []
        for k in xrange(2*N-1):
            if buf[k][j] == m:
                cnt += 1
                sel.append(k)
        if cnt == 2:
            if j==0:
                r_flag[0] = sel[0]
                l_flag[0] = sel[1]
                for l in xrange(N):
                    grid[l][0] = buf[sel[0]][l]
                    grid[0][l] = buf[sel[1]][l]
                # for g in grid:
                #     print g
            else:
                r_flag[j] = sel[0]
                l_flag[j] = sel[1]
        else:
            # print cnt
            candidate = [buf[x][j] for x in xrange(2*N-1)]
            # print candidate
            # remove exist one
            for j in buf[sel[0]]:
                candidate.remove(j)
            print "Case #%d:" % (i+1), " ".join([str(x) for x in sorted(candidate + [m])])
            o.write("Case #%d: " % (i+1))
            o.write(" ".join([str(x) for x in sorted(candidate + [m])]))
            o.write("\n")
            break

