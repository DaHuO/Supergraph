numTest = 0
inputs = [] 

def getOppositeChar(c):
	if c == '+':
		return '-'
	elif c == '-':
		return '+'

def reverse(aList, to):
	#print 'before ' + str(aList)
	start = 0;
	end = to
	for i in range(0, (to+1)/2):
		startC = aList[start]
		endC = aList[end]
		aList[start] = getOppositeChar(endC)
		aList[end] = getOppositeChar(startC)
		start = start + 1
		end = end - 1
		
		if start >= end:
			break
	if to % 2 == 0:
		aList[start] = getOppositeChar(aList[start])
	#print 'after ' + str(aList)
	
def calc(input):
	cList = list(input)
	print 'Original input ' + str(cList)
	
	count = 0
	rearPos = len(cList) - 1
	
	while True:
		rearPos = findRearPos(cList, '-', rearPos)
		if rearPos == -1:
			print 'Result output ' + str(cList)
			return count
			
		if cList[0] != '-':
			frontPos = findFrontPos(cList, '-') - 1
			reverse(cList, frontPos)
		else:
			reverse(cList, rearPos)
		count = count + 1

	#print 'pos front find ' + str(findFrontPos(cList, '+'))
	#print 'pos front find ' + str(findFrontPos(cList, '-'))
	#print 'pos front find ' + str(findRearPos(cList, '+', len(cList) - 2))
	#print 'pos front find ' + str(findRearPos(cList, '-', len(cList) - 2))
	#print 'reversed input ' + str(cList)


def findFrontPos(aList, target):
	for i in range(0, len(aList)):
		if aList[i] == target:
			return i
	return -1
	
def findRearPos(aList, target, start):
	for i in range(start,-1,-1):
		if aList[i] == target:
			return i;
	return -1

def main():
	f = open("B-large.in", 'r')
	numTest = int(f.readline())
	print '# of test : ' + str(numTest)
	
	lines = f.read().splitlines()
	
	for line in lines:
		inputs.append(line)
	f.close()
	
	f = open("output_large_test2.txt", 'w')
	
	for i in range(0, len(inputs)):
		output = 'Case #%d: %d' % (i+1, calc(inputs[i]))
		print output
		f.write(output + '\n')
	f.close()
	
if __name__ == "__main__":
    main()