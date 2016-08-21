N = int(input())

revMap = { '+' : '-', '-' : '+' }

def flip(s):
	ret = ""
	for i in range(len(s)):
		c = s[i]
		c2 = revMap[c]
		ret = ret + c2
	return ret
		
def countFlips(remStack):
	#print("cf: " + remStack)
	rem = remStack.rstrip('-')
	remCount = len(rem)
	
	if remCount == 0:
		return 1
	else:
		remFlipped = flip(rem)
		subCount = countFlips(remFlipped)
		return 1 + subCount
	
	
def pancakes(initialStack):
	
	rem = initialStack.rstrip('+')
	remCount = len(rem)
	
	if remCount == 0:
		return 0
	else:
		return countFlips(rem)

		
for i in range(1, N+1):
	M = str(input())
	flips = pancakes(M)
	print('Case #' + str(i) + ': ' + str(flips))
	

