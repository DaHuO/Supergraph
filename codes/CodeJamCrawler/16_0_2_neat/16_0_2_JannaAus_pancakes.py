
import time

def flipPancakes(stack):
	counter = 1
	top = stack[0]
	nextPC = stack[1]

	#always flip at least top pancake
	stack[0] = stack[0] * -1


	while len(stack) != sum(stack) and len(stack) > counter and top == nextPC:
		stack[counter] = stack[counter] * -1
		counter = counter + 1
		nextPC = stack[counter]

	return stack

def flipStack(stack, flipCounter):
	# print flipCounter, stack
	if len(stack) == sum(stack):
		return flipCounter
	elif len(stack) == abs(sum(stack)):
		return flipCounter + 1
	else:
		return flipStack(flipPancakes(stack), flipCounter + 1)

start_time = time.time()
# f = open("sampleB.txt")
# f = open("B-small-attempt0.in")
f = open("B-large.in")
result = open('B-large-output.txt', 'w')

cases = int(f.readline().rstrip())
for x in xrange(0, cases):
	inStack = f.readline().rstrip().replace("+", "1,").replace("-", "-1,").split(",")
	inStack = filter(None, inStack)
	stack = map(int, inStack)
	caseResult = "Case #"+str(x+1)+": " + str(flipStack(stack, 0)) + "\n"
	result.write(caseResult)
f.close()
result.close()

# print flipStack([-1, -1, 1, -1], 0)
# print flipPancakes([-1, -1, 1, -1])

print("--- %s seconds ---" % (time.time() - start_time))
