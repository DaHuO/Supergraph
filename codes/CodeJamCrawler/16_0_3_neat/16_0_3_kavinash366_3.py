import math
import random
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, 1000))
def base2decimal(s,b):
	length = len(s)
	tsum = 0
	for i in range(length-1,-1,-1):
		tsum = tsum + pow(b,i)*int(s[length-i-1])
	return tsum

def nfactor(n):
	print n
	for x in range(2,n):
		if(n%x==0):
			return x
def factors(n):    
	# return [x for x in range(1, n+1) if n % x == 0]
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, 1000) if n % i == 0)))
test = raw_input()
[n,j] = raw_input().split(" ")
[n,j] = [int(n),int(j)]


numbers = []
constant = pow(2,n-1)+1
# print bin(constant)[2:]
while(len(numbers)<j):
	currentNumber = random.randrange(0,pow(2,n-2))*2+constant
	# print bin(currentNumber)[2:]
	e = 0
	for i in range(2,11):
		if(is_prime((base2decimal(bin(currentNumber)[2:],i)))==True):
			e = 1
	if(e==0):
		if(bin(currentNumber)[2:] not in numbers):
			numbers.append(bin(currentNumber)[2:])

print numbers
print "Case #1: "
for number in numbers:
	string = number+" "
	for i in range(2,11):
		x = factors(int(number,i))
		nu = 1
		for e in x:
			if(e!=1 and e!=int(number,i)):
				nu = e
				break
		string = string + str(nu) + " "
	print string[0:len(string)-1]

# print factors(int("1001101111000011",9))
# print base2decimal("10011",2)