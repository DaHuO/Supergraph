#!/usr/bin/python

def get_digits(n, digits):
	while n > 0:
		rem = n % 10
		if rem not in digits:
			digits.append(rem)
		n = n / 10

	# print('digits: ' + str(digits))
	return digits

def count_sheep(n, q):
	# print('n to count: ' + str(n))
	pre = 'Case #' + str(q) + ': '
	if n == 0:
		print pre + 'INSOMNIA'
	else:
		digits = []
		i = 1
		while len(digits) < 10:
			m = i * n
			i += 1
			get_digits(m, digits)
		print pre + str(m) 

if __name__ == "__main__":
	with open("data") as f:
		content = f.read().split()
		
		for i in range(1, len(content)):
			count_sheep(int(content[i]), i)