


def description():
	print """
	Input

		The first line of the input gives the number of test cases, T. 
		T test cases follow. 
		Each consists of one line with a string S, 
		each character of which is either + (which represents a pancake that is initially happy side up) 
		or - (which represents a pancake that is initially blank side up). 
		The string, when read left to right, represents the stack when viewed from top to bottom.

	Output

		For each test case, output one line containing 
		Case #x: y
		, where x is the test case number (starting from 1) 
		and y is the minimum number of times you will need to execute the maneuver to get all the pancakes happy side up. 
"""

# it is sufficient to count the number of changes between + and -
# where we append an extra + to the bottom because we will have to make a manouver if the last one is a -
def solve(x):
	xi = x + "+"
	return str(xi.count("+-") + xi.count("-+"))



filename = "B-large"

with open(filename + ".in","r") as f:
	content = f.read().splitlines()

no_of_cases = int(content[0])


outputs = []
for c in content[1:]:
	result = solve(c)
	print result, c
	outputs.append(result)

with open("" + filename +".out","w") as f:
	for o in range(len(outputs)):
		f.write("Case #"+ str(o+1) + ": " + outputs[o] + "\n")
