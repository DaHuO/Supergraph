def numOfPoints(s):
	n = 0
	for i in range(0,len(s)-1):
		if(s[i] != s[i+1]):
			n = n + 1
	return n

def calculateMin(s):
	if (s[-1] == '-'):
		return numOfPoints(s)+1
	else:
		return numOfPoints(s)

num = input()
for i in range(1,num+1):
	s = str(raw_input())
	print 'Case #{i}: {MIN}'.format(i=i,MIN=calculateMin(s))