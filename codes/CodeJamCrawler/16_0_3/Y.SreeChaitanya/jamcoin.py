import itertools
import math
##from math import sqrt; from itertools import count, islice
list=["".join(seq) for seq in itertools.product("01", repeat=15)]
divset=[]
pcandidates=[]
count=0
jamcoins=[]
for x in list:
		#q="10"+x+x+x+x+"01"
		#n="10"+x+x[::-1]+x+x[::-1]+"01"
		#v="10"+x[::-1]+x+x+x[::-1]+"01"
		#y="10"+x+x+x+x+"11"
		#z="11"+x+x+x+x+"11"
		#w="11"+x+x+x+x+"01"
		#pcandidates.append(q)
		#pcandidates.append(n)
		#pcandidates.append(y)
		#pcandidates.append(w)
		z="1"+x+x+"1"
		pcandidates.append(z)
#print(pcandidates)

def is_prime(n):
    global divset
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        divset.append(2)
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            divset.append(divisor)
            return False
    return True

##def isPrime(n):
  ##  return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
print("Case #1:")
for x in pcandidates:
	divset=[]
	count=0
	##print(x)
	for i in range(2,11):
		num=int(x,i)
		if(is_prime(num)==True):
			count=0
			break
		else:
			count+=1
	if(count==9):
		jamcoins.append(x)
		op=x
		for div in divset:
			op+=" "+str(div)
		print(op)
		##print("hey" +str(x))
	if(len(jamcoins)==500):
		break




