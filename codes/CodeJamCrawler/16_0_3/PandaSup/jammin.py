import random
import math

def checkPrime(n):
	if n%2==0:
		return 2
	else:
		for i in range(3, math.ceil(math.sqrt(n)), 2):
			if n%i == 0:
				return i
	return -1
	
def generateJC(N):
	jc = list()
	jc.append(str(1))
	for i in range(N-2):
		jc.append(str(0))
	jc.append(str(1))	
	return jc
	
def jam(N, J):
	count = 1
	JC = generateJC(N)
	JC = ''.join(JC)
	while count <= J:	
		factList = []
		for i in range(2,11):
			temp = int(JC, i)
			fact = checkPrime(temp)
			if fact!= -1:
				factList.append(fact)
		if len(factList) == 9:
			count += 1
			print("{} ".format(int(JC)), end="")
			for j in range(9):
				print("{} ".format(factList[j]), end="")		
			print()
		JC = int(JC, 2)
		JC += 2
		JC = bin(JC).lstrip('0b')
	
tc = int(input())
for i in range(1,tc+1):
	N, J = map(int, input().split())
	print("Case #{}:".format(i))
	jam(N, J)
	
