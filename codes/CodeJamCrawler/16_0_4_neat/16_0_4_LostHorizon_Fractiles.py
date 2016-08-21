def solve(N):
	K,C,S = N
	X = (" ").join([str(i+1) for i in range(0,K)])
	print X
	return X


def dosolve(f,g):
	d = f.read().split("\n")
	n = int(d[0])

	j = 1
	for i in range(1,n+1):
		print "\n Case no " + str(i) + "\n"
		answer = solve(map(int,d[i].split(" ")))
		print answer
		g.write ("Case #" + str(i) + ": " + answer + "\n")

	return 0

def solve_large():
	g = open("A-large-final.txt","w")
	f = open("A-large.in","r")
	dosolve(f,g)

def solve_small():
	g = open("D-small-out0.txt","w")
	f = open("D-small-attempt0.in","r")
	dosolve(f,g)

def solve_examples():
	g = open("D-eg-out.txt","w")
	f = open("D-eg.in","r")
	dosolve(f,g)
	
solve_examples()
# solve_small
# solve_large