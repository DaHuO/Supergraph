numDict = {}
numList = [0,1,2,3,4,5,6,7,8,9]

def insertInDict(i,num):
	global numDict
	temp , n = 1,1
	while check() != True:
		n = i * num
		temp = n
		#print n
		while n > 0:
			r = n%10
			if r not in numDict:
				numDict[r]=1
			n = int(n/10)
		i += 1
	i -= 1
	return temp

def check():
	global numList,numDict
	count = 0
	for i in range(0,len(numList)):
		if numList[i] in numDict:
			count += 1
	if count == 10:
		return True
	else:
		return False

i = 1
k = 0
t = input()
for k in range(1,t+1):

	numDict = {}
	n = input()
	if n == 0:
		print str("CASE #%d: INSOMNIA"%k)
		continue
	print str("CASE #%d: %d"%(k,insertInDict(i,n)))