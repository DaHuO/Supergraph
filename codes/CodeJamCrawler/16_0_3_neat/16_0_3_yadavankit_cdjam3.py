def to_binary(n):
	s = ""
	while n > 0:
		if n % 2:
			s = "1" + s
		else:
			s = "0" + s
		n //= 2
	return s

def to_base(val, base):
	output = 0
	for c in val:
		output *= base
		if c == "1":
			output += 1
	return output

def get_divisor(val):
	for i in range(2, val - 1):
		if val % i == 0:
			return i

def is_prime_number(n):
	n = abs(int(n))  # 0 and 1 are not primes
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n ** 0.5) + 1, 2):
		if n % x == 0:
			return False
	return True

def test(val):
	if val[-1] == "0":
		return False
	is_ok = True
	for base in range(2, 11):
		val_in_base = to_base(val, base)
		if is_prime_number(val_in_base):
			is_ok = False
	if is_ok:
		print(val, end="")
		for base in range(2, 11):
			print(" " + str(get_divisor(to_base(val, base))), end="")
		print()
		return True
	return False

def process(n, j):
	val = 2**(n-1)
	found = 0
	while found < j:
		if test(to_binary(val)):
			found += 1
		val += 1
        
num_of_test = int(input())

for test_id in range(1, num_of_test + 1):
	n, j = (int(i) for i in input().split())
	print("Case #" + str(test_id) + ":")
	process(n, j)
