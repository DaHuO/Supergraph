def condenser(stack):
	index = 0
	while index + 1 < len(stack):
		while index + 1 < len(stack) and stack[index] == stack[index + 1]:
			del stack[index + 1]
		index += 1

def minFlips(stack):
	flips = 0
	while len(stack) > 0:
		last = len(stack) - 1
		if stack[last] == '+':
			del stack[last] 
		elif last == 0:
			del stack[last]
			flips += 1
		elif stack[last] == stack[0]:
			for i in range(0, len(stack)):
				if stack[i] == '+':
					stack[i] = '-'
				else:
					stack[i] = '+'
			flips += 1
		else:
			del stack[0]
			flips += 1
	return flips

case = 1
inputs = []
with open('B-large.in') as f:
	for line in f:
		line = line.split()
		if line:
			inputs.append(list(line[0]))
del inputs[0]
for i in range(0, len(inputs)):
	condenser(inputs[i])
	print('Case #' + str(case) + ': ' + str(minFlips(inputs[i])))
	case += 1