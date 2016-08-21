#srtart with the top pancake. Its not about orientaton, its about alighnment.
#Work your way down, until one of the pancakes is out of alignment, then fip everything above the disorderly pancake.

file = open('B-large.txt')

lines = file.readlines()

panflip = open('pan2flip.txt','w')

testcases = int(lines[0])

i = 1

while i <= testcases:
	stackst = lines[i]
	stack = []
	g = 0
	while g < len(stackst):
		stack.append(stackst[g])
		g = g + 1
	if stack[-1] == '\n':
		stack = stack[:-1]

	
	r = 1
	flips = 0
	while r < len(stack):

		if stack[r] != stack[r-1]:
			if stack[r] == '+':
				c = 0
				while c < r:
					stack[c] = '+'
					c = c + 1
				flips = flips + 1


			elif stack[r] == '-':
				c = 0
				while c < r:
					stack[c] = '-'
					c = c + 1
				flips = flips + 1


		else:
			r = r + 1
	
	if stack[0] == '-':
		flips = flips + 1
	

	panflip.write('Case #' + str(i) + ': ' + str(flips) + '\n')
	
	i = i + 1
	
panflip.close()
file.close()