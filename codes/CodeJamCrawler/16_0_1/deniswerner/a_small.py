


def description():
	print """
	Input

		The first line of the input gives the number of test cases, T. 
		T test cases follow. 
		Each consists of one line with a single integer N, the number Bleatrix has chosen.

	Output

		For each test case, output one line containing 
		Case #x: y, 
		where x is the test case number (starting from 1) 
		and y is the last number that Bleatrix will name before falling asleep, 
		according to the rules described in the statement. 
"""


def solve(x):
	if x == 0:
		return "INSOMNIA"
	numbers = set()
	for i in xrange(1,1000):
		xi = i*x
		curr = [int(ii) for ii in str(xi)]
		numbers.update(curr)
		if len(numbers) == 10:
			return str(xi)

	return "INSOMNIA"


filename = "A-large"

with open(filename + ".in","r") as f:
	content = f.read().splitlines()

no_of_cases = int(content[0])


outputs = []
for c in content[1:]:
	result = solve(int(c))
	print c,result
	outputs.append(result)

with open("" + filename +".out","w") as f:
	for o in range(len(outputs)):
		f.write("Case #"+ str(o+1) + ": " + outputs[o] + "\n")
