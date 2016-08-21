def SplitNumber(number):
	list = [int(i) for i in str(number)]
	return list

def UpdateCheckList(number):
	NumberList = SplitNumber(number)
	for element in NumberList:
		CheckList[element] = 1

def CheckListCompleted(listToCheck):
	sum = 0
	for element in listToCheck:
		sum += element
	if sum == 10:
		return True
	else:
		return False

LoopSize = int(raw_input())
#print "LoopSize: {}".format(LoopSize)

i = 0

while i < LoopSize:
	N = int(raw_input())
	#print "N: {}".format(N)
	multiplier = 1
	countLoop = 1
	CheckList = [0,0,0,0,0,0,0,0,0,0]
	if(N==0):
		print "Case #{}: {}".format(i + 1, 'INSOMNIA')
	else:
		while  not CheckListCompleted(CheckList):
			UpdateCheckList(multiplier*N)
			#print "multiplier * N: {}".format(multiplier*N)
			#print "CheckList: {}".format(CheckList)
			countLoop += 1
			multiplier += 1
			#print "coutloop: {} | multiplier: {}".format(countLoop, multiplier)	
		print "Case #{}: {}".format(i + 1, (multiplier - 1) * N)
	i += 1

