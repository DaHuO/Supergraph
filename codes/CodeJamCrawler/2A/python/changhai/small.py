#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
	
def check(a):
	r = list(a)
	while len(r) > 1:
		r2 = []
		for i in range(0, len(r), 2):
			if r[i]==r[i+1]: return 0
			if r[i]=="P" and r[i+1]=="R":
				r2.append("P")
			if r[i]=="R" and r[i+1]=="P":
				r2.append("P")
			if r[i]=="P" and r[i+1]=="S":
				r2.append("S")
			if r[i]=="S" and r[i+1]=="P":
				r2.append("S")
			if r[i]=="R" and r[i+1]=="S":
				r2.append("R")
			if r[i]=="S" and r[i+1]=="R":
				r2.append("R")
		r = r2
	return 1
	

def solve(P,R,S):
	a = "P"*P +  "R"*R + "S"*S
	for per in itertools.permutations(a):
		if check(per):
			return "".join(per)
	return "IMPOSSIBLE"
	
import sys, itertools
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N,R,P,S = f.readline().strip().split()
	N, R, P, S = int(N), int(R), int(P), int(S)
	rt = solve(P,R,S)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()