import sys

def get_digits(n):
	if n == 0:
		yield 0

	while n > 0:
		yield n % 10
		n /= 10

def beatrix(n):
	if n == 0:
		return 'INSOMNIA'

	digits = [0] * 10
	i = 0

	while not all(digits):
		i += 1
		for d in get_digits(i * n):
			digits[d] += 11

	return i * n;

def main():
	num_of_cases = int(raw_input())
	for i in xrange(num_of_cases):
		n = int(raw_input())
		print 'Case #%s: %s' % (i + 1, beatrix(n))

if __name__ == '__main__':
	main()