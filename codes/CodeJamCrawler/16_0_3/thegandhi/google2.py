import math
from random import randint

content = []
with open("/home/rubal/C-small-attempt3.in") as f:
    content = f.readlines()

secondline = content[1]

thelist = secondline.split()

thelistofoutput = []

n = int(thelist[0])
j = int(thelist[1])
#print "j: " + str(j)

b = 0

print "Case #1: "

while b != j:
	
	xy = ''.join(["%s" % randint(0, 1) for num in range(0, n-2)])
	number = str(1) + xy + str(1)
	def basefunction(number, base):
		thenumber = str(number)
		thesize = len(thenumber)-1
		i = 0
		add = 0
		while thesize>=0:
			add = add + int(thenumber[thesize])*pow(base,i)
			thesize = thesize - 1
			i = i+1
		return add

	def findifprime(numbers):
		flag = 0
		for i in range(2, int(math.ceil(math.sqrt(numbers)))+1):
			#print "number: " + str(numbers) + " i: " + str(i)
			if(numbers%i==0):
				thelistofoutput.append(i)
				flag = 1
				break
		if flag==1:
			return 0 #not a prime number
		else:
			return 1 #prime number
		
	def ifjamcoin():
		for i in range(2,11):
			numbers = basefunction(number,i)
			returnprime = (findifprime(numbers))
			if returnprime == 1:
				return 1
				break

	returnprime = ifjamcoin()

	
	if returnprime != 1:
		print number,
		for i in thelistofoutput:
			print i,
		print 
		b = b + 1
	
	thelistofoutput = []
	
