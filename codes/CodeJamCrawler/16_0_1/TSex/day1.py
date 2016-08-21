import re

f = open('sheep2.txt', 'r')
g = open('1.txt', 'w')


iterationCount = int(f.readline())

upCounter = 0





while iterationCount > 0:
	
	outputLine = ''
	
	upCounter = upCounter + 1
	
	curArrayList = [[0,0] , [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], [8,0], [9,0]]
	
	currentNumber = int(re.sub("[^0-9]", "", f.readline()))
	
	if currentNumber != 0:
		
		factor = 1
		
		while not curArrayList[0][1] == curArrayList[1][1] == curArrayList[2][1] == curArrayList[3][1] == curArrayList[4][1] == curArrayList[5][1] == curArrayList[6][1] == curArrayList[7][1] == curArrayList[8][1] == curArrayList[9][1] == 1:
		
			currentNumberString = str(int(currentNumber*factor))
		
			for c in currentNumberString:
				e = 0
				while e <= len(curArrayList)-1:
					if curArrayList[e][1] == 0 and curArrayList[e][0] == int(c):
						#print curArrayList[e]
						curArrayList[e][1] = 1
					e = e+1
				
			
					
			#print (currentNumber*factor)
			factor = factor + 1
		g.write("Case #" + str(upCounter) + ": " + str(int(currentNumber*(factor-1))) + "\n")
		#print currentNumber
		#print factor
		
					
					
	else:
		g.write("Case #" + str(upCounter) + ": INSOMNIA\n")
		
	iterationCount = iterationCount - 1
	#print iterationCount
		
	
	
	
	
	
	