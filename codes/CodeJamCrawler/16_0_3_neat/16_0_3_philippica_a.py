f = open ("a.txt",'w')
printable = 1
def isPrime(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if i * i > n :
			break
		if i > 200:
			return True
		if n % i == 0:
			if printable == 0:
				f.write (str(i) + " ")
			return False
	return True

def fun(x,bas):
	now = 1
	ret = 0
	while x != 0:
		v = x % 2
		x = x // 2
		if v == 1:
			ret = ret + now
		now = now * bas
	return ret


def check(x):
	for i in range(2, 11):
		u = fun(x, i)
		if isPrime(u):
			return False
	return True

n = 32
x = 2 ** (n - 1)
bin(x).replace('0b','')
for mid in range(x, x * 2 - 2):
	if mid % 2 == 1:
		if check(mid):
			printable = 0
			f.write(bin(mid).replace('0b','') + ' ')
			check(mid)
			printable = 1
			f.write("\n")