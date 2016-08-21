from itertools import product
from math import ceil, sqrt

def description():
	print """
	Input

		The first line of the input gives the number of test cases, T. 
		T test cases follow. 
		Each consists of one line with three integers: K, C, and S.

	Output

		For each test case, output one line containing 
		Case #x: y, 
		where x is the test case number (starting from 1) 
		and y is either IMPOSSIBLE 
		if no set of tiles will answer your question, 
		or a list of between 1 and S positive integers, 
		which are the positions of the tiles that will answer your question. 

		The tile positions are numbered from 1 for the leftmost tile to KC for the rightmost tile. 
		Your chosen positions may be in any order, but they must all be different. 
"""


def solve(k,c,s):
	if c == 1:
		if s < k:
			return "IMPOSSIBLE"
		else:
			return " ".join([str(kk) for kk in range(1,k+1)])
	else:
		needed = k/2 + (k%2)
		if s < needed:
			return "IMPOSSIBLE"

		else:
			retval = ""
			# gotta get two each
			# first block, second place
			# third block, fourth place 
			# recalculate needed as we make the last one separate if we have an extra free spot
			needed = k/2
			for i in range(needed):
				block = i*2 + 1
				row = block+1
				retval += str((block-1)*k + row) + " "
			# gotta hit the last block
			if (k%2) != 0:
				block = needed * 2 + 1
				retval += str((block)*k )
			return retval


filename = "D-small-attempt0"

with open(filename + ".in","r") as f:
	content = f.read().splitlines()

no_of_cases = int(content[0])


outputs = []
for ci in content[1:]:
	k,c,s = ci.split(" ")
	result = solve(int(k),int(c),int(s))
	print k,c,s," - ",result
	outputs.append(result)

with open("" + filename +".out","w") as f:
	for o in range(len(outputs)):
		f.write("Case #"+ str(o+1) + ": " + outputs[o] +"\n")
