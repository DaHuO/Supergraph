import sys
import random
import math
N = 16
J = 50
#First we do some computation generating the binaries numbers and then, once done just get the result and print, faster execution
arrBin ={}
randBinList = lambda n: [random.randint(0,1) for b in range(1,n+1)]

while len(arrBin)<=110:
	randd = randBinList(N-2)
	a=''.join(str(s) for s in randd)
	arrBin["1{}1".format(a)]=[]

bases = 10
cont=0

print("Case #1:")

def isprime(num):
	raiz = math.sqrt(num);
	if num == 2:
		return True
	elif(num < 2 or num % 2 == 0):
		return False
	
	for i in range(3, int(raiz)):
		if num % i == 0:
			return False
		i+=2
	return True

def divisorGenerator(n):
	for i in range(2,int(n/2+1)):
		if n%i == 0:
			return i

for s in arrBin:
	
	if cont<J:
		flag = False
		arrDiv = []
		for b in range(2,bases+1):
			num = int(s, b)
			if isprime(num):
				flag=False
				break
			arrDiv.append(divisorGenerator(num))
			flag=True
		if flag:
			cont+=1
			res = " ".join(map(str,arrDiv))
			print("{} {}".format(s, res))


