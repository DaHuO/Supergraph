content = []
with open("/home/rubal/B-large.in") as f:
    content = f.readlines()

x = int(content[0])

for b in range(1, x+1):
	thelist = []
	count = 0
	for char in content[b]:
		thelist.append(char)
	
	newlist = thelist
	index = len(thelist) - 1

	def findtheminus(thelist, index):
		while(index >= 0):
			if thelist[index] is '-':
				break
			index = index - 1
		return index	

	def thefunc(thelist, index):
		newlist = []
		theindexofminus = findtheminus(thelist, index)	
		for i in range(0,theindexofminus+1):
			if thelist[i] is '-':
				newlist.append('+')
			else:
				newlist.append('-')
	
		thelist = newlist + thelist[theindexofminus+1:]
		return thelist
				 

	while(1):
		if '-' in thelist:
			count = count + 1
			thelist = thefunc(thelist, index)
		else:
			print "Case #" + str(b) + ": " + str(count)
			break
	
