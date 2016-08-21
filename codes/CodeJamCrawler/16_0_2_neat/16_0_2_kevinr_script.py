def check(stack):
	for s in stack:
		if s == False:
			return False
	return True

def maneuver(stack):
	temp = stack[0]
	for i in range(len(stack)):
		if stack[i] == temp:
			if stack[i] == True:
				stack[i] = False
			elif stack[i] == False:
				stack[i] = True
		else:
			break
	return stack

file_in = open("input.txt", "r")
file_out = open("output.txt", "w")
file_out.truncate()
lines = []
lines_out = []

for line in file_in:
	lines.append(line)

i = -1
for line in lines:
	k = False
	if i == -1:
		i = 0
		k = True
	if k == True :
		continue
	else :
		stack = []
		for c in line:
			if c == '+':
				stack.append(True)
			elif c == '-':
				stack.append(False)
		counter = 0
		while check(stack) == False:
			stack = maneuver(stack)
			counter += 1
		lines_out.append(counter)

for i in range(int(lines[0])):
	file_out.write("Case #" + str(i + 1) + ": " + str(lines_out[i]) + "\n")
