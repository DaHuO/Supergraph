import math

def serch_prime(n):
	#len = int(math.sqrt(n) + 2)
	len = 1000
	for i in range(2,len):
		if n % i == 0:
			return i;
	return -1; 


def interpret(v, n):
	ret = 0;
	c = 1;
	while (v > 0):
		if (v & 1):
			ret += c;
		c *= n
		v = v >> 1	
	return ret;


def tenToTwo(v,n):

	c = ""

	for i in range(0,n):
		if v % 2 == 0:
			c = "0" + c
		else: 
			c = "1" + c
		
		v = v / 2
	
	return c





print "Case #1:"



n = 32
j = 500


base = 1 << (n - 1);
base |= 1;

count =  (1 << (n -2)) - 1

while count >= 0:
	v = base | (count << 1);
	isOk = True
	memo = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	for k in range(2,11):
		val = interpret(v,k);
		ret = serch_prime(val);
		if ret == -1: 
			isOk = False;
			break;
		memo[k] = ret;
		
	if isOk:
		s = str (tenToTwo(v,n))
		for p in range(2, 11): 
			s+= " " + str(memo[p])

		print(s)
		j-=1
		if j <= 0: 
			break
			
		
	count -= 1
