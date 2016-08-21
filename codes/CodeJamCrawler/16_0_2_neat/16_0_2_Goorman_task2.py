file = open("B-large.in.txt", "r")

def Solve(x):
	cur  = x[0]

	dif = 0

	for letter in x[1:]:
		if letter != cur:
			dif += 1
			cur = letter

	if x[-1] == "-":
		dif += 1

	return dif

input = [row.strip() for row in file][1:]

answer = [Solve(x) for x in input]

for i, ans in enumerate(answer):
	print "Case #" + str(i+1) + ": " + str(ans)
