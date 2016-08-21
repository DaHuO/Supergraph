def FlipPancakes(listPancakes, position):
	pancakesTop = listPancakes[0:position]
	pancakesBottom = listPancakes[position:]
	#print "pancakesTop: {}".format(pancakesTop)
	#print "pancakesBottom: {}".format(pancakesBottom)
	pancakesTop = pancakesTop[::-1]
	pancakesTopNew = ''
	for element in pancakesTop:
		pancakesTopNew = pancakesTopNew + switchSidePancake(element)
		#print element
	return (pancakesTopNew + pancakesBottom)

def CountNegPancakes(pancakes):
	count = 0
	for element in pancakes:
		if(element=='-'):
			count += 1
	return count

def CountPosPancakes(pancakes):
	count = 0
	for element in pancakes:
		if(element=='+'):
			count += 1
	return count

def switchSidePancake(PancakeSide):
	if PancakeSide == '+':
		return '-'
	else:
		return '+'

def organizePancakesPositive(moviments, pancakes):

	#print "OP POS - Moviments: {}".format(moviments)
	#print "OP POS - pancakes: {}".format(pancakes)

	#pancakes == 1
	if(len(pancakes)==1):
		if(pancakes[0]=='-'):
			moviments += 1
		else:
			moviments += 0
		return moviments
	
	#pancakes == 2 
	if(len(pancakes)==2):
		if(pancakes[0]=='+'and pancakes[1]=='-'):
			moviments += 2 
		if(pancakes[0]=='-'and pancakes[1]=='+'):
			moviments += 1
		if(pancakes[0]=='-'and pancakes[1]=='-'):
			moviments += 1
		return moviments

	#pancakes > 2
	if(len(pancakes) > 2):
		#last element is '-' and first is '+'
		if(pancakes[-1]=='-' and pancakes[0]=='+'):
			pancakes = FlipPancakes(pancakes,0)
			pancakes = FlipPancakes(pancakes,len(pancakes))
			moviments +=2
		elif(pancakes[-1]=='-' and pancakes[0]=='-'):
			pancakes = FlipPancakes(pancakes,len(pancakes))
			#pancakes = FlipPancakes(pancakes,len(pancakes))
			moviments +=1
		#if(pancakes[-1]=='+' and pancakes[0]=='+'):
		#	pancakes = FlipPancakes(pancakes,len(pancakes))
		#	#pancakes = FlipPancakes(pancakes,len(pancakes))
		#	moviments +=1
		#print "OP POS > 2 - pancakes: {}".format(pancakes)
		return organizePancakesPositive(moviments, pancakes[0:len(pancakes) - 1])

def organizePancakesNegative(moviments, pancakes):

	#print "OP NEG - Moviments: {}".format(moviments)
	#print "OP NEG - pancakes: {}".format(pancakes)

	#pancakes == 1
	if(len(pancakes)==1):
		if(pancakes[0]=='+'):
			moviments += 1
		else:
			moviments += 0
		return moviments
	
	#pancakes == 2 
	if(len(pancakes)==2):
		if(pancakes[0]=='-'and pancakes[1]=='+'):
			moviments += 2 
		if(pancakes[0]=='+'and pancakes[1]=='-'):
			moviments += 1
		if(pancakes[0]=='+'and pancakes[1]=='+'):
			moviments += 1
		return moviments

	#pancakes > 2
	if(len(pancakes) > 2):
		#last element is '-' and first is '+'
		if(pancakes[-1]=='+' and pancakes[0]=='-'):
			pancakes = FlipPancakes(pancakes,0)
			pancakes = FlipPancakes(pancakes,len(pancakes))
			moviments +=2
		elif(pancakes[-1]=='+' and pancakes[0]=='+'):
			pancakes = FlipPancakes(pancakes,len(pancakes))
			#pancakes = FlipPancakes(pancakes,len(pancakes))
			moviments +=1
		#if(pancakes[-1]=='-' and pancakes[0]=='-'):
		#	pancakes = FlipPancakes(pancakes,len(pancakes))
		#	#pancakes = FlipPancakes(pancakes,len(pancakes))
		#	moviments +=1
		#print "OP NEG > 2 - pancakes: {}".format(pancakes)
		return organizePancakesNegative(moviments, pancakes[0:len(pancakes) - 1])


def ReducePancakes(pancakes):
	pancakesNew = ''
	p1 = 0
	p2 = 1
	size = len(pancakes)
	pancakesNew = pancakesNew + pancakes[p1]
	while p2 < size:
		if(pancakes[p1] != pancakes[p2]):
			p1 = p2
			pancakesNew = pancakesNew + pancakes[p1]
		p2 += 1
	return pancakesNew

##############################################

LoopSize = int(raw_input())
#print "LoopSize: {}".format(LoopSize)

i = 0

while i < LoopSize:
	pancakes = raw_input()
	#print "MAIN - pancakes: {}".format(pancakes)
	if (len(pancakes) > 2):
		pancakes = ReducePancakes(pancakes)
	#print "MAIN - Reduce pancakes: {}".format(pancakes)
	#print "MAIN - CountPosPancakes: {}".format(CountPosPancakes(pancakes))
	#print "MAIN - len pancakes: {}".format(len(pancakes))
	if(CountPosPancakes(pancakes) == (len(pancakes))):
		print "Case #{}: {}".format(i + 1, 0)
	else:
		numMovimentsPos = organizePancakesPositive(0, pancakes)
		numMovimentsNeg = organizePancakesNegative(1, pancakes)
		#print "MAIN - numMovimentsPos: {}".format(numMovimentsPos)
		#print "MAIN - numMovimentsNeg: {}".format(numMovimentsNeg)
		print "Case #{}: {}".format(i + 1, min(numMovimentsNeg, numMovimentsPos))
	i += 1
	#pancakes = FlipPancakes(pancakes, len(pancakes)-1)
	#print pancakes
	#print 'size: {}'.format(len(pancakes))
	#print 'positives: {}'.format(CountPosPancakes(pancakes))
	#print 'negatives: {}'.format(CountNegPancakes(pancakes))