import random

def num_from_base(num, base):
	result = 0
	exp = 1
	while num > 0:
		result += (num % 10) * exp
		num /= 10
		exp *= base
	return result

def get_small_divisor(num):
	i = 2
	while i < 1000:	# Pretty good limit for known dataset size
		if num % i == 0:
			return i
		i += 1
	return 0

def get_divisors(num):
	divisors = []
	for base in range(2, 11):
		divisor = get_small_divisor(num_from_base(num, base))
		if divisor is not 0:
			divisors.append(divisor)
		else:
			return False
	return divisors

def generate_coin_num(N):
	num = '1'
	for i in range(N-2):
		num += str(random.randint(0, 1))
	num += '1'
	return int(num)

def find_numbers(N, J):
	found = set()
	while len(found) < J:
		current = generate_coin_num(N)
		divisors = get_divisors(current)
		if divisors:
			found.add((current, ' '.join(map(str, divisors))))
	return found

T=input()
assert T==1, 'Bad input'
N, J = [int(v) for v in raw_input().split()]
result = find_numbers(N, J)
print("Case #1:")
for num, divisors in result:
	print("%s %s" % (num, divisors))