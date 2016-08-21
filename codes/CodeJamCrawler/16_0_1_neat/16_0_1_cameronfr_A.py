text = open("/Users/cameronfranz/Documents/Learning/Projects/Code Jam/2016/A-large.in")
numCases = int(text.readline())

def seenAllDigits(list):
	result = True;
	for i in range(len(list)):
		if (list[i]==0):
			result = False;
	return result

for i in range(numCases):
	n = int(text.readline())
	if (n==0): 
		result="INSOMNIA"
	else:
		numlist = [0,0,0,0,0,0,0,0,0,0]
		for k in range(1,100):
			N = k * n
			for j in range(len(str(N))):
				numlist[int(str(N)[j])] = numlist[int(str(N)[j])] + 1
			if seenAllDigits(numlist):
				result = N
				break
			
			
	print ("Case #" + str(i+1) + ": " + str(result))
				