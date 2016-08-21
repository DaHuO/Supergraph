caseCount = int(input())
outfile = open("panOut.txt", "w")
for x in range(caseCount):
	stack = list(input())
	flipCount = 0
	for elem in range(len(stack))[::-1]:
		if stack[elem] == "-":
			flipCount += 1
			for pom in range(len(stack[:elem])):
				if stack[pom] == "-":
					stack[pom] = "+"
				else:
					stack[pom] = "-"
	outfile.write("Case #{}: {}\n".format(x+1, flipCount))
