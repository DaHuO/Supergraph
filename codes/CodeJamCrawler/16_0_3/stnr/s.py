import math
bits = 32
needed = 500

def find_div(num):
	i = 2
	while (i < math.sqrt(math.sqrt(math.sqrt(num)))):
		if (num % i == 0):
			return i
		i+=1
	return 0
	
count = 0
print "Case #1:"

for i in xrange(0,2**(bits - 2)):
	num = "1"+bin(i)[2:].zfill(bits-2)+"1"
	result = num
	prime = False
	
	for j in xrange(2, 11):
		div = find_div(int(num, j))
		if (div == 0):
			prime = True
			break
		else:
			result += " " + str(div)
	if (prime == False):
		count+=1
		print result
		
	if count == needed:
		break
		
			
	
