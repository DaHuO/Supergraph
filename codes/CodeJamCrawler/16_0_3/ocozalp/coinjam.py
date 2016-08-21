def convert(binary_val, newbase):
	total = 0
	current = 1
	while binary_val > 0:
		total += (binary_val % 2) * current
		binary_val /= 2
		current *= newbase
	return total

def is_prime(num):
	if num % 2 == 0:
		return False
	n = 3
	while n * n <= num and n <= 1000:
		if num % n == 0:
			return False
		n += 2
	return True

def get_first_divisor(num):
	if num % 2 == 0:
		return 2
	n = 3
	while n * n <= num:
		if num % n == 0:
			return n 
		n += 2 

def print_numbers(numbers):
	print 'Case #1:'
	for number in numbers:
		line = ["{0:b}".format(number), str(get_first_divisor(number))]
		for i in xrange(3, 11):
			line.append(str(get_first_divisor(convert(number, i))))

		print ' '.join(line)

def main():
	m = 2 ** 31 
	numbers = list()
	for i in xrange(1, m, 2):
		num = m + i
		if not is_prime(num):
			last_f = 2
			for j in xrange(3, 11):
				newnum = convert(num, j)
				if not is_prime(newnum):
					last_f = j
				else:
					break

			if last_f == 10:
				numbers.append(num)
				if len(numbers) == 500:
					break

	print_numbers(numbers)

if __name__ == '__main__':
	main()
