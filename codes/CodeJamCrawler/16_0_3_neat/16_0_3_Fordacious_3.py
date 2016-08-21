def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    

def isDivisor (a,b):
	return a%b == 0

def valueInBase (v, base):
	val = 0
	p = 0
	while (v > 0):
		val += v % 2 * (base**p)
		v = int(v/2)
		p += 1
	return val

def divisors(value):
	divisors = []
	for base in range(2, 11):
		baseval = valueInBase(value, base)
		for divisor in range(2, int(baseval / 2)):
			if isDivisor(baseval, divisor):
				divisors.append(divisor)
				break
	return divisors

def isjamcoin(value):
	if bin(value)[-1] == '0' or bin(value)[2] == '0':
		return False
	for base in range(2, 11):
		baseval = valueInBase(value, base)
		if (is_prime(baseval)):
			return False
	return True

def tostring (divs):
	s = ""
	for i in divs:
		s += str(i) + ' '
	return s

N = 16
J = 50

lower = 2**(N-1)
higher = 2**(N)

print ("Case #1:")

for i in range(lower, higher):
	pass
	if isjamcoin(i):
		print ("{0:b} ".format(i) + tostring(divisors(i)))
		J -= 1
		if (J == 0):
			break
# 	else:
# 		print (str(i) + " -")

#if __name__ == '__main__':
	#print(isjamcoin(42))
	#for i in range(1,11):
		#print (valueInBase(35, i))
	#print(divisors(63))
