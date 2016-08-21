import itertools
import time
import math

count = 0
MIN = 500

#print str(bin(4294967295))

def base(N, b): 
        res = 0 
        for i in range(0,32):
                n = N % 10  
                res += n * (b ** i)
                N = N /10 
    
        return res 

def isprime(n):
	#print " checking if {} is prime".format(n)
	if n == 2:
        	return True
	if n == 3:
        	return True
	if n % 2 == 0:
	        return False
	if n % 3 == 0:
	        return False

	i = 5 
	w = 2 

	start = time.time()
	while i * i <= n:
        	if n % i == 0:
		        return False	

	        i += w
	        w = 6 - w 
		curr  = time.time()
		if curr - start > 0.5:
			return True

	return True

def getDivisor(N):
        i = 2
        while i < math.sqrt(N) + 1:
                if N % i == 0:
                        return i
                i += 1


print "Case #1:"

#for i in xrange(32769,65536,2): 16 digits
#for i in itertools.count(2147483649,2):  32 digits  

#for i in xrange(32769,65536,2):
for i in itertools.count(2147483649,2):    
	str_num = str(bin(i))
	num = long(str_num[2:])
	#print str_num, num
	ll = []
	mm = []

	check = False

	for j in range(2,10):
		x =  base(num, j)
		ll.append(x)
		if isprime(x):
			check = True
			break
		mm.append(getDivisor(x))

	if isprime(num):
		check = True

	if check == False:
		print num, 
		for k in mm:
			print k,
		print  getDivisor(num)
	
		count += 1
		if count >= MIN:
			exit()
	
