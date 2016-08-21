def solve(X):
	while "++" in X:
		X = X.replace("++","+")
	while "--" in X:
		X = X.replace("--","-")
	print X
	if X[-1] == "+":
		return len(X) - 1
	else:
		return len(X)
	return

def dosolve(f,g):
	d = f.read().split("\n")
	n = int(d[0])

	j = 1
	for i in range(1,n+1):
		print "\n Case no " + str(i) + "\n"
		answer = solve(d[i])
		print answer
		g.write ("Case #" + str(i) + ": " + str(answer) + "\n")

	return 0
	
def solve_large():
	g = open("B-large-out.txt","w")
	f = open("B-large.in","r")
	dosolve(f,g)

def solve_small():
	g = open("B-small-out0.txt","w")
	f = open("B-small-attempt0.in","r")
	dosolve(f,g)

def solve_examples():
	g = open("B-eg-out.txt","w")
	f = open("B-eg.in","r")
	dosolve(f,g)
	
# solve_examples()
# solve_small()
solve_large()