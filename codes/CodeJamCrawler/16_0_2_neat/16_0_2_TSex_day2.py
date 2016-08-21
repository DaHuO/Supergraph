f = open('pancake.txt', 'r')
g = open('1.txt', 'w')

iterationCount = int(f.readline())

upCounter = 0

while iterationCount > 0:

	upCounter = upCounter + 1

	initialStack = str(f.readline())
	
	doneFlag = 0
	
	flipCount = 0
	
	reverseStack = list(initialStack.rstrip())
	
	
	
	leadingChar = ''
		
	charCount = 0
		
	i = 0
	
	#print reverseStack
		
	for c in reverseStack:
		charCount = charCount + 1
			
		if leadingChar == '' and ( c == '+' or c == '-'):
			leadingChar = c
			#print leadingChar
				
		elif c != leadingChar and ( c == '+' or c == '-'):
			#print c
			#print charCount
			#print 'flip count increment'
			flipCount = flipCount + 1
			leadingChar = c
	
	#checkStack = initialStack[::-1]	
	#print reverseStack[len(reverseStack)-1]
	if (reverseStack[len(reverseStack)-1] == '-'):
		
		#print "1 extra flip"
		flipCount = flipCount + 1
			
	g.write("Case #" + str(upCounter) + ": " + str(flipCount) + "\n")
	iterationCount = iterationCount - 1
				
				
			