input() # ignore amount
l = input()
l = l.split(" ")
N = int(l[0])
J = int(l[1])

# N kohaline binary
# J erinevat

divs = []

def isprime(n):
	global divs
	""""pre-condition: n is a nonnegative integer
	post-condition: return True if n is prime and False otherwise."""
	if n < 2: 
		return False;
	if n % 2 == 0:		 
		divs.append(str(2))
		return n == 2  # return False
	k = 3
	while k*k <= n:
		if n % k == 0:
			divs.append(str(k))
			return False
		k += 2
		if(k>14):
			return False # ehk saab ikka piisavalt
	return True

def tonum(s,base):
	s = s[::-1]
	res = 0
	for i in range(len(s)):
		# print(s[i])
		res += int(s[i])*(base**i)
	return res
		
def checkones(s):
	if(s[0]=="0" or s[-1]=="0"):
		return False

def valid(s):
	global divs
	divs = []
	for i in range(2,11):
		# print(s,i,tonum(s,i))
		if(isprime(tonum(s,i))):
			return False
	return True
		
# print(tonum("1010",2))

_x = N
count = 0
print("Case #1:")

for i in range(2**(_x-1)+1,2**_x,2):
	if(count>=J):
		break
	s = bin(i)[2:].zfill(_x)
	if(valid(s) and len(divs)==9):
		print(s," ".join(divs))
		count=count+1
# print(count)