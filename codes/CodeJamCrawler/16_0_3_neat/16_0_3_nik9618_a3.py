import math

f = open('/Users/nik9618/Downloads/test.txt', 'r')
case = 0
f.readline()

hashPrime = {};

def tobase(n, b):
	
	ct = len(n)-1
	mult = 1;
	sum = 0;
	for i in n:
		sum = sum + int(i) * b**ct
		ct-=1
	return sum

def isPrime(n):

	if(n in hashPrime) : 
		return hashPrime[n];

	for i in range(2,int(math.sqrt(n))+1):
		if(n%i ==0 ): 
			hashPrime[n] = False;
			return i

	hashPrime[n] = True
	return -1

tc = 1;
for line in f.readlines():
	line = line.split("\n")[0].split(' ')

	N = int(line[0])
	J = int(line[1])
	# print N , J

	currentCounting = 0;

	ans = []
	anscode = [];
	while(len(ans) < J and currentCounting <2**(N-2)):

		bin = "{0:b}".format(currentCounting)
		bin =  "1"+bin.zfill(N-2)+"1"

		passCriterion = True
		code = []
		# print bin
		for i in range(2,11):
			x = isPrime(tobase(bin,i))
			if(x==-1):
				passCriterion = False
				break;
			else:
				code.append(x)

		print ans;
		
		if(passCriterion):
			ans.append(bin);
			anscode.append(code)

		currentCounting+=1

	# print ans

	print "Case #"+str(tc) +": "
	tc+=1

	for i in range(len(ans)):
		print ans[i],
		for j in anscode[i]:
			print j,
		print ''
