#debug 
def pr(*a):
	return
	for x in a: print x,
	print

def index(d):
	if d==0: return 0
	if d > 0: return d
	if d < 0: return -d-1
	
def calc(N, K, P):
	prb = [0] * (2*K+1)
	prb[0] = 1
	for i in range(K/2): #i pair
		a = P[i]
		b = P[N-i-1]
		d2 = a*b
		d0 = a*(1-b)+b*(1-a)
		d_2 = (1-a)*(1-b)
		pr(a,b,d2,d0,d_2)
		prb2 = [0] * (2*K+1)
		for d in range(-i*2, 2*i+1, 2):
			pr(d, index(d), index(d+2), index(d-2), "----")
			prb2[index(d)] += prb[index(d)]*d0
			prb2[index(d+2)] += prb[index(d)]*d2
			prb2[index(d-2)] += prb[index(d)]*d_2
		prb = prb2
	return prb[0]
	
def solve(N,K,P):
	ret = 0
	for i in range(2**N):
		s = bin(i)[2:]
		s = "0"*(N-len(s))+s
		choose = []
		for i in range(N):
			if s[i]=='1':
				choose.append(P[i])
		if len(choose)==K:
			c = calc(K,K,choose)
			ret = max(ret, c)
	return ret
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	P = [float(x) for x in f.readline().strip().split()]
	pr(N, K, P)
	P.sort()
	rt = solve(N,K,P)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()