S = 6

MAX_CASES = 2**S - 1

def createStack(num):
	ret = bin(num)
	ret = ret[2:len(ret)]
	return ((S - len(ret)) * "0" + ret).replace("0", "-").replace("1", "+")

# stack after flipping n pancakes
def flip(stack, n):
	ret = ""
	for i in range(0, n):
		c = stack[n - 1 - i]
		if c == "-":
			ret += "+"
		else:
			ret += "-"
	ret += stack[n:]
	return ret

def isHappy(stack):
	ret = True
	for c in stack:
		ret = ret and (c == "+")
	return ret

def search(stack, d, D):
	if isHappy(stack):
		return (0, [])
	if (d > D):
		return (50000, [])
	minFlip = 10000
	flipped = 0
	for i in range(1, S + 1):
		nextStack = flip(stack, i)
		res = search(nextStack, d + 1, D)
		score = 1 + res[0]
		if score < minFlip:
			minFlip = score
			flipped = [i] + res[1]
	return (minFlip, flipped)

# heuristic: choose N which maximizes number of + in the tail
def plussesInEnd(stack):
	count = 0
	for i in range(len(stack) - 1, -1, -1):
		if stack[i] == "+":
			count += 1
		else:
			break
	return count

# check if my approach produces same results as actual DFS
def NerasTactics(stack):
	# import pdb; pdb.set_trace()
	# newStack = stack
	# flips = 0
	# while not isHappy(newStack):
	# 	maxi = 0
	# 	maxTails = 0
	# 	for i in range(0, len(stack)):
	# 		next = flip(newStack, i)
	# 		if plussesInEnd(next) > maxi:
	# 			maxi = plussesInEnd(next)
	# 			maxTails = i
	# 	flips += 1
	# 	newStack = flip(newStack, maxTails)
	# return flips
	breaks = 0;
	current = stack[0]
	for c in stack:
		if c != current:
			breaks += 1
			current = c
	if stack[0] == "+":
		if breaks % 2 == 0:
			return breaks
	if stack[0] == "-":
		if breaks % 2 == 1:
			return breaks
	return breaks + 1



D = 10
results = {}
for case in range(0, MAX_CASES):
	stack = createStack(case)
	#print stack
	for i in range(3, 10):
		res = search(stack, 0, i)
		if res[0] < 5000:
			#print res
			results[stack] = res[1]
			break

for case in results:
	if len(results[case]) != NerasTactics(case):
		print "Discrepancy. Case: %s Real: %d Neras: %d" % (case, len(results[case]), NerasTactics(case)) 

