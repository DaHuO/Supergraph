import collections

f = open('large1.in')
T = int(f.readline().strip())

oneDict = [{"Z":1, "E":1 ,"R":1,"O":1}, #Z 
{"T":1, "W":1, "O":1}, #W
{"S":1, "I":1, "X":1}, #X
{"S":1, "E":2, "V":1, "N":1}, #S
{"F":1, "I":1, "V":1, "E":1}, #V
{"F":1, "O":1, "U":1, "R":1}, #F
{"E":1, "I":1, "G":1, "H":1, "T":1}, #G
{"N":2, "I":1, "E":1}, #I
{"O":1, "N":1, "E":1}, #O
{"T":1, "H":1, "R":1, "E":2}
]

twoDict = [0,2,6,7,5,4,8,9,1,3]

for k in range(T):
	original = f.readline()
	aDict = {}
	for i in original:
		if i == '\n':
			continue
		if i in aDict:
			aDict[i] += 1
		else:
			aDict[i] = 1
	bDict = {}
	for z in range(10):
		num = twoDict[z]
		alpha = oneDict[z]
		minNum = 2**99
		for alp, j in alpha.iteritems():
			if alp in aDict:
				if aDict[alp]/j < minNum:
					minNum = aDict[alp]/j
			else:
				minNum = 0
				break
		if minNum  > 0:
			for alp,j in alpha.iteritems():
				aDict[alp] -= minNum*j
				bDict[num] = minNum
	for alp, j in aDict.iteritems():
		if j != 0:
			print alp
	od = collections.OrderedDict(sorted(bDict.items()))
	oneString = ""
	for num, minNum in od.iteritems():
		oneString += (str(num) * minNum)
	print "Case #%d: %s" %(k+1, oneString)
		