import sys, random


pr = [True] * 10001
for i in range(len(pr)/2):
    if not pr[i]: continue
    for j in range(i, len(pr)/2):
        v = (2*i+3) * (2*j+3)
        v = (v-3)/2
        if v>=len(pr): break
        pr[v] = False

prime = {}
prime[2] = {}
for i in range(len(pr)):
    if pr[i]:
    	prime[ 2*i+3 ] = {}

print >> sys.stderr, "prime count=", len(prime)


for p in prime.keys():
    for b in range(2, 11):
        for n in range(0, 32):
            prime[p][b * 32 + n] = (b**n) % p

random.seed()
print >> sys.stderr, "aa"

rund = set()

def run(N):
    global rund
    v = [1] * N
    for n in range(1, N-1):
        v[n] = random.randint(0, 1)

    sv = ''
    for i in range(len(v)): sv += str(v[ len(v) - i - 1 ])
    if sv in rund: return False
    rund.add( sv )

    print >> sys.stderr, v
   
    ret = []
    for b in range(2, 11):
        fp = -1

        nv = 0
        for n in range(0, N):
            if v[n] == 1: nv += b ** n
        
        if nv in prime: break
        for p in prime.keys():
            c = 0
            for n in range(0, N):
                if v[n] == 1: c += prime[p][b*32 +n]
            if c % p == 0:
                fp = p 
                break
        if fp == -1: 
            break
        ret.append(fp)

    if len(ret) == 9:
    	print >> sys.stderr, ret
        

        print sv,
        for i in ret: print i,
        print ""

        return True

    return False 


for q in range(int(sys.stdin.readline())):
    N,J = map(int, sys.stdin.readline().split())
    print 'Case #%d:' % (q+1)


    while J>0:
        if run(N): 
           J = J-1
