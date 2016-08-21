

LIMIT = 10000000;
sieve = [True] * LIMIT 
primes = []

def fill_sieve():
	i = 2;
	while i * i <= LIMIT:
		if sieve[i] == True:
			primes.append(i);
			j = i << 1
			while j < LIMIT:
				sieve[j] = False;
				j += i
		i+=1

	while i < LIMIT:
		if sieve[i] == True:
			primes.append(i);
		i+=1

def isprime(n, divs):
	if n==0:
		return False
	temp = n;
	j = 0
	while True:
		if j >= len(primes):
			return True;
		if primes[j] * primes[j] > temp:
			break
		if primes[j] == 0:
			print("FUCK", n)
		if temp % primes[j] == 0:
			divs.append(primes[j])
			return False
		j += 1
	return True

def binf(n, width):
	buf = [0] * 40
	for i in range(width):
		buf[width-i-1] = n & 1;
		n >>= 1;
	for i in range(width):
		print(buf[i], end = "")
	print(" ", end = "")


print("Case #1: ")
fill_sieve()
count = 0
t = int(input())
n, m = map(int, input().split())
limit = (1 << (n-2)) - 1
k = 1 << (n-1)
divs = []
for i in range(LIMIT+1):
	j = (i<<1) + k + 1
	good = True
	divs.clear()

	for b in range(2,11):
		conv = int(bin(j)[2:], b)
		#print(conv)
		if isprime(conv, divs) == True:
			good = False
			break

	if good == True:
		count += 1
		binf(j, n)
		for d in divs:
			print(d, end = " ");
		print("")

	if count == m:
		break