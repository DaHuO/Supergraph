import sys
import string
import numpy

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

n = ['ZERO','ONE','TWO','THREE','FOUR',
    'FIVE','SIX','SEVEN','EIGHT','NINE']

u = {'Z': 0, 'W': 2, 'U': 4, 'X': 6, 'G': 8}

# Find chars used
ch = {}
for numstr in n:
    for c in numstr:
        ch[c] = 0

def count(str):
    cnt = {}
    for c in ch:
        cnt[c] = 0
    for c in str:
        cnt[c] += 1
    return cnt

def cnt2vec(cnt):
    r = []
    for ch in sorted(cnt):
        r.append(cnt[c])
    return r

# count number of times ch is in str
def hits(ch,str):
    return len(str) - len(str.replace(ch,''))

def sub(count, num):
    for x in n[num]:
        count[x] = count.get(x,0) - 1
        if count[x] < 0:
            print "**** ERRROR ****"
            print count
    return

def solve(S):
    A = []
    B = []

    for c in ch:
        aa = []
        for i in range(10):
            aa.append(hits(c,n[i]))
        A.append(aa)
        B.append(hits(c,S))

    a0 = numpy.array(A)
    b0 = numpy.array(B)
    #print a0
    #print b0
    lq = numpy.linalg.lstsq(a0,b0)
    #print lq
    #print lq[0]
    x = [int(round(v)) for v in lq[0]]
    print x

    res = []
    for i in range(10):
        res.extend(str(i) * x[i])
    return ''.join(res)

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            S = f.readline().strip()
            print S
            outf.write('Case #{}: '.format(x+1))
            outf.write(solve(S))
            outf.write('\n')
