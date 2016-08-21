def Flip_The_Chips(pancakes):
	stack = []
	for char in pancakes:
		stack.append(char)
	while stack and stack[-1] == '+':
		del stack[-1]
	sides = ['-','+']
	if stack:
		lookOutFor = stack[0]
	flips = 0
	for index in stack:
		if index == lookOutFor:
			flips = flips + 1
			lookOutFor = sides[lookOutFor == '-']
	return (flips)


times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ": " + str(Flip_The_Chips(str(raw_input()))))