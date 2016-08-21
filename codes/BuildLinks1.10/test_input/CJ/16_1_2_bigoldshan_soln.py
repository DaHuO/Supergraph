import sys
from collections import deque
inp = sys.stdin
inp = open("B-small-attempt1.in","r")
outp = open("out","w")
#outp = sys.stdout

def read_inp():
    return inp.readline().strip()

T = int(read_inp())


def place(a,r,i,t,force=False):
    r0 = [0]*len(r)
    if t == 'row':
        if not force:
            for j in xrange(len(r)):
                if a[i][j] != 0 and a[i][j]!=r[j]:
                    return False, None
                
                for k in xrange(0,i):
                    if a[k][j]!=0 and a[k][j] >= r[j]:
#                         print a, r, i,t,force,k,j,a[k][j],a[i][j]
                        return False,None                    

                for k in xrange(i+1,N):
                    if a[k][j]!=0 and a[k][j] <= r[j]:
#                         print a, r, i,t,force,k,j,a[k][j],a[i][j]
                        return False,None                    
                
        for j in xrange(len(r)):
            r0[j] = a[i][j]
            a[i][j] = r[j]
    if t == 'col':
        if not force:
            for j in xrange(len(r)):
                if a[j][i] != 0 and a[j][i]!=r[j]:
                    return False, None

                for k in xrange(0,i):
                    if a[j][k]!=0 and a[j][k] >= r[j]:
#                         print a, r, i,t,force,k,j,a[j][k],a[j][i]
                        return False,None                    

                for k in xrange(i+1,N):
                    if a[j][k]!=0 and a[j][k] <= r[j]:
#                         print a, r, i,t,force,k,j,a[j][k],a[j][i]
                        return False,None                    

        for j in xrange(len(r)):
            r0[j] = a[j][i]
            a[j][i] = r[j]
    return True, r0

for t in xrange(1,T+1):
    N = int(read_inp())
    
    ss = []
    for s in xrange(2*N-1):
        ss.append([int(tt) for tt in read_inp().split()])

    a = [[0]*N for _ in xrange(N)]
    def arrange(a, i, occupied):
        s = ss[i]
        succ = False
        for r in xrange(N):
            for c in ['row','col']:
                if (r,c) in occupied:
                    continue
                
                succ,r0 = place(a, s, r, c)
                if succ:
                    occupied.add((r,c))
                    if i < len(ss)-1:
                        succ = arrange(a, i+1, occupied)
                        if not succ:
                            place(a,r0,r,c,True)
                            occupied.remove((r,c))
                if succ:
                    break
            if succ:
                break
        return succ
    
    succ = arrange(a, 0, set())
    assert succ
    
    #print a
    counts = {}

    for i in xrange(N):
        r = tuple(a[i])
        if r not in counts:
            counts[r] = 0
        counts[r]+=1
    
    for i in xrange(N):
        r = tuple([a[j][i] for j in xrange(N)])
        if r not in counts:
            counts[r] = 0
        counts[r]+=1
        
    scounts= {}
    for s in ss:
        r = tuple(s)
        if r not in scounts:
            scounts[r] = 0
        scounts[r] += 1
    
    missing = None
    for k in counts:
        if k not in scounts or counts[k]>scounts[k]:
            missing = k
            break
        
    outp.write("Case #%d: %s\n"%(t,' '.join([str(s) for s in missing])))

outp.close()