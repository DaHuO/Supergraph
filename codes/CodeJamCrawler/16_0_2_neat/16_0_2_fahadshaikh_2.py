
def main():
	fp = open("case.txt","r")
	out = open("result.txt","w")

	cache = fp.readlines()
	cache = cache[1:]
	
	caseCount = 1
	for S in cache:
		S = S.strip()
		
		listS=list(S)
		
		noOfFlips = 0
		
		while True:
			index = getIndex(listS)
			if index != -1 : 
				listS = flip(listS,index)
				noOfFlips +=1
			else:
				outString = "Case #%d: %d\n" % (caseCount , noOfFlips)
				out.write(outString)
				break
		caseCount +=1
		
	print "saved"

def flip(S,index):
	#print "initial : ", S
	for i in range(index,-1,-1):
		if(S[i]=='+'):
			#print "char at %d is %c" % (i,S[i])
			S[i]='-'
		else:
			#print "char at %d is %c" % (i,S[i])
			S[i]='+'
	return S
			
def getIndex(S):
	index=-1
	count = 0
	for i in S:
		if i=='-':
			index = count
		count +=1
	return index
	
if __name__ =='__main__':
	main()
