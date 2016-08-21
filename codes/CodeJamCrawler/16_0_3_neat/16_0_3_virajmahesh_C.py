from math import sqrt

def interpret_as(string, base):
	n = 0
	for i in xrange(len(string)):
		n += (base**(len(string) - i - 1)) * string[i]
	return n

def is_prime(n):
	for i in xrange(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return False
	return True

def non_trivial_divisor(n):
	for i in xrange(2, int(sqrt(n) + 1)):
		if n % i == 0:
			return i
	raise 'Error'

def solve(n):
	string = map(int, '1' + format(n, '0{0}b'.format(N - 2)) + '1')
	numbers = []
	for b in xrange(2, 11):
		number = interpret_as(string, b)
		numbers.append(number)
		if is_prime(number):
			return False, string, numbers
	return True, string, numbers

out = open('C.small.out', 'w')

N = 16
J = 50
C = 0
limit = 2**(N - 2)

out.write('Case #1:\n')
for i in xrange(limit):
	result, coin, numbers = solve(i)
	if result:
		C += 1
		divisors = map(non_trivial_divisor, numbers)
		out.write('{0} {1}\n'.format(''.join(map(str, coin)), ' '.join(map(str, divisors))))

	if C == J:
		break

out.close()