def main(K,C,S):
	l = []
	for x in xrange(2,K+1):
		l += [str(x)]
	if K == S:
		l = []
		for x in xrange(1, K + 1):
			l += [str(x)]
	if K - 1 > S:
		returnString = "IMPOSSIBLE"
	elif K == 2 and S == 1:
		returnString = "IMPOSSIBLE"
	else:
		returnString = " ".join([str(i) for i in l])
	return returnString

def fileHandler(inName):
	returnString = ""
	f = open(inName,'r')
	i = 1
	init = True
	for line in f:
		if init == True:
			init = False
			continue
		returnString += "Case #" + str(i) + ": " + main(int(line.split()[0]),int(line.split()[1]),int(line.split()[2])) + "\n"
		i += 1
	f.close()
	w = open('results.txt','w')
	w.write(returnString)
	w.close()

fileHandler("D-small-attempt0 (1).in")