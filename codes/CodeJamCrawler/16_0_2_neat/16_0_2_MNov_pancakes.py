def firstIndex(needle, haystack):
	if needle not in haystack:
		return len(haystack)
	return min([index for index,straw in enumerate(haystack) if straw == needle])

def solveSingle(s):
	steps = 0
	while "-" in s:
		s = flip(s, max(firstIndex("-",s), firstIndex("+",s)))
		steps += 1
	return steps
	
def flip(s, n):
	return invert(s[n-1::-1]) + s[n:]
	
def invert(s):
	return "".join(["-" if x == "+" else "+" for x in s])
	
def solveFile(filename):
	problem = open(filename)
	sol = open(filename + ".solved", 'w')
	problem.readline()
	i = 1
	for line in problem:
		sol.write("Case #" + str(i) + ": " + str(solveSingle(line.strip())) + "\n")
		i += 1