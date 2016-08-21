# BasicInputA.py
import math

t = int(input())
nada = int('0b0000000000',2)
todo = int('0b1111111111',2)

for loopNum in range(1, t + 1):
 	orgN = int(input())
 	treshold = 0
 	numLength = 0
 	try:
 		numLength = int(math.log10(orgN)) + 1
 		treshold = pow(10,numLength)
 	except:
 		n = "INSOMNIA"
 	else:
 		s = nada
 		n = 0
 		while s !=todo:
	 		n += orgN
	 		n2 = int(n)
	 		if(n > treshold):
	 			numLength += 1
	 			treshold *= 10
	 		for x in range(0,numLength):
	 			rem = int(n2%10)
	 			tempBinary = ((1 << rem))
	 			s = s|tempBinary
	 			n2 //= 10



 	print("Case #{}: {}".format(loopNum, n))
	#check out .format's specification for more formatting options


