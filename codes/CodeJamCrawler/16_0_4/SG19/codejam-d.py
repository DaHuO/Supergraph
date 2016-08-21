def solver(cases):
	with open("codejam-d.out", "w") as f:
		for i, c in enumerate(cases, start=1):
			f.write("Case #%d: %s\n" % (i, helper(c)))
		f.close()

def helper(case):
	params = case.split(" ")
	K = int(params[0])
	C = int(params[1])
	S = int(params[2])
	pos = []
	for i in range(0, K**C, int(K**C / S)):
		pos.append(str(i + 1))
	return " ".join(pos)

if __name__ == "__main__":
	with open('D-small-attempt0.in', 'r') as f:
		f.readline()
		cases = f.readlines()
		solver(cases)
		f.close()