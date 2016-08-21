def findMissing(inputLines):
	resultdict = {}
	for i in range(len(inputLines)):
		for j in range(len(inputLines[0])):
			if resultdict.has_key(inputLines[i][j]):
				resultdict[inputLines[i][j]] += 1
			else:
				resultdict[inputLines[i][j]] = 1
	resultList = []
	for key in resultdict.keys():
		#print key, resultdict[key]
		if resultdict[key] % 2 == 1:
			resultList.append(int(key))
	resultList.sort()
	return resultList




def comp(lista, listb):
	listlen = len(lista)
	for i in range(listlen):
		if lista[i] < listb[i]:
			return -1
		if lista[i] > listb[i]:
			return 1
	return 0


# a=[1,3,7,4,3]
# def comp(a,b):
# 	if a<b:
# 		return -1
# 	if a == b:
# 		return 0
# 	else:
# 		return 1
# d = a.sort(comp)
# print a
# exit()




if __name__ == "__main__":
	inputfile = open('B-large.in').read().split('\n')
	filehandler = open('large.out', 'w')

	inputLen = len(inputfile)

	currentLine = 1
	currentRound = 1
	casesNum = int(inputfile[0])
	while currentLine <= inputLen - 1:
		if len(inputfile[currentLine]) == 0:
			break
		#print len(inputfile[currentLine])
		N = int(inputfile[currentLine])
		inputMatrix = []
		for i in range(2*N-1):
			tmpList = inputfile[currentLine+i+1].split()
			inputMatrix.append(tmpList)
		print inputMatrix
		resultList = findMissing(inputMatrix)
		print 'case %s' % currentRound
		print resultList

		#print 'Case #%s: %s' % (currentRound, outputStr)
		filehandler.write('Case #%s:' % (currentRound))

		for i in range(len(resultList)):
			filehandler.write(' %s' % resultList[i])
		filehandler.write('\n')
		currentRound += 1
		currentLine += 2 * N
	filehandler.close()



