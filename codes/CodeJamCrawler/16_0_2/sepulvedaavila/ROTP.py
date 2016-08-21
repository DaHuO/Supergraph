from itertools import groupby

def darthPancakius(plist):
	myList = [x[0] for x in list(groupby(plist))]
	if myList[-1] == "+":
		myList = myList[:-1]
	return len(myList)

t = int(raw_input())
for i in xrange(1, t + 1):
	n = raw_input()
	print "Case #{0}: {1}".format(i, darthPancakius(n))