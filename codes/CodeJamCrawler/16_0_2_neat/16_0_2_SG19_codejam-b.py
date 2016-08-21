def solver(cases):
	with open("codejam-b-large.out", "w") as f:
		for i, c in enumerate(cases, start=1):
			f.write("Case #%d: %d\n" % (i, helper(c)))
		f.close()

def helper(stack):
	flips = stack.count("+-") * 2
	if stack[0] == "-":
		flips += 1
	return flips

if __name__ == "__main__":
	with open('B-large.in', 'r') as f:
		f.readline()
		cases = f.readlines()
		solver(cases)
		f.close()