def solve(S):
	A = S[0]
	for i in S[1:]:
		if i >= A[0]:
			A = i + A
		else:
			A = A + i
		# print A, i, i < A[0]

	return A

def dosolve(f,g):
	d = f.read().split("\n")
	n = int(d[0])
	j = 1
	for i in range(1,n+1):
		print solve(d[i])
		g.write ("Case #" + str(i) + ": " + str(solve(d[i])) + "\n")

	return 0

def solve_large():
	g = open("A-large-final.txt","w")
	f = open("A-large.in","r")
	dosolve(f,g)

def solve_small():
	g = open("A-small-out0.txt","w")
	f = open("A-small-attempt0.in","r")
	dosolve(f,g)

def solve_examples():
	g = open("A-eg-out.txt","w")
	f = open("A-eg.in","r")
	dosolve(f,g)
	
# solve_examples()
# solve_small()
solve_large()