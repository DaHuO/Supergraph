def allOk(stack):	
	for c in stack:
		if c=="-":
			return False
	return True
	
def toggle(stack):
	for i in range(0,len(stack)):
		if stack[i] == '+':
			stack[i] = '-'
		else:
			stack[i] = '+'	
	return stack
	
def reverse(stack):
	return stack[::-1]
	
def flip(stack,i):
	if i == len(stack)-1:
		return toggle(reverse(stack))
	result = toggle(reverse(stack[:i+1])) + stack[i+1:]
	return result

def getFlipIndex(stack):
	index = 0
	prevVal = stack[0]
	for i in range(0,len(stack)):
		if stack[i]!= prevVal:
			return i-1
		prevVal = stack[i] #Unnecessary technically
		index = index+1
	return index
	
def calculateFlips(testCase):
	stack = list()
	for a in testCase:
		stack.append(a)	
	count=0
	while (not allOk(stack)):
		count = count + 1;		
		flipIndex = getFlipIndex(stack)		
		stack = flip(stack,flipIndex)		
	return count

def main():
	testCount = raw_input()
	testCases=list()
	for i in range (0,int(testCount)):
		testCase = raw_input()
		testCases.append(testCase)

	for i in range(0,len(testCases)):
		testCase = testCases[i]
		result = calculateFlips(testCase)	
		print "Case #"+str(i+1) + ": " + str(result)
		

if __name__ == '__main__':
	main()