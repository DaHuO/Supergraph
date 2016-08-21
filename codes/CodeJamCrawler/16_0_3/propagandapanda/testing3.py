import math

def is_not_prime(n):
	last = math.floor(math.sqrt(n))
	for i in range(2, last + 1):
		if n % i == 0:
			return i
	return False

def not_prime_all_bases(n):
	factors = []
	for i in range(2, 11):
		num = 0
		temp = n
		count = 0
		while temp != 0:
			temp, digit = temp // 10, temp % 10
			if (digit == 1):
				num += int(math.pow(i, count))
			count += 1
		#print(i, num, n)
		prime = is_not_prime(num)
		if prime:
			factors.append(prime)
		else:
			return False
	return factors

def getCoinJam(n, j, case):
	print('Case #' + str(case) + ':')
	for i in range(0, int(math.pow(2, n - 2))):
	#for i in range(1):
		#print(bin(i)[2:])
		b = int(str(1) + str(0) * (n - 2 - len(bin(i)[2:])) + bin(i)[2:] + str(1))
		#print(b)
		#print(b)
		base = not_prime_all_bases(b)
		if base:
			print(b, ' '.join((str(x) for x in base)))
			j -= 1
		if j == 0:
			return

case = 1
inputs = []
with open('test.in') as f:
	for line in f:
		line = line.split()
		if line:
			line = [int(i) for i in line]
			inputs.append(line)
del inputs[0]
for i in range(0, len(inputs)):
	getCoinJam(inputs[i][0], inputs[i][1], case)
	case += 1

