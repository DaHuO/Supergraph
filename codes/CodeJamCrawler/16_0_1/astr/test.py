import collections
import math
# debug=False
# with open('A-small-practice.in') as f:
debug=True
with open('A-large.in') as f:
	content = f.readlines()

def GetLastNumberBeforeSleep(N):	
	if(N==0):
		return "INSOMNIA"
	digit,currentNumber={'0','1','2','3','4','5','6','7','8','9'},N
	while len(digit)!=0:
		tempDigit=set(digit)
		strCurrentNumber=str(currentNumber)
		for x in digit:
			if(x in strCurrentNumber):
				tempDigit.remove(x)
		if(len(tempDigit)==0):
			return currentNumber
		else: 
			currentNumber+=N
			digit=tempDigit
		


numOfTestCase=int(content.pop(0))
for x in range(numOfTestCase):
	N=int(content.pop(0))
	# print("N: "+str(N))
	print("Case #%d: %s"%(x+1,GetLastNumberBeforeSleep(N)))
