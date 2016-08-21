import os

inf = open('input.in')
inp = inf.read().split('\n')
inf.close()
outf=open('output','w')

T = int(inp.pop(0))

def cover(pos, cov, c, k, rem):
    print pos, cov, c, k, rem
    if c == 0 or rem == 0:
        return pos
    else:
        return cover(pos + (k**(c-1))*(cov-1),cov+1,c-1,k,rem-1)

for i in range(T):
    outf.write('Case #%d: '%(i+1))
    K, C, S = [int(x) for x in inp.pop(0).split(' ')]
    if C*S < K:
        outf.write('IMPOSSIBLE')
    else:
        covered = 1
        while covered <= K:
            outf.write('%d '%(cover(0,covered,C,K,K-covered+1)+1))
            covered += C
    outf.write('\n')


outf.close()