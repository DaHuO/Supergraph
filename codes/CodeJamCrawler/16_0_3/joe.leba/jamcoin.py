from math import *

class Jamcoin:
	def __init__(self, file_in, file_out):
		with open(file_in, 'r') as fi:
			with open(file_out, 'w') as fo:
				num_cases = int(fi.readline())

				for i in range(1, num_cases + 1):
					fo.write('Case #{}:\n'.format(i))
					n, j = map(lambda x: int(x), fi.readline().split(' '))
					jams = self.generate_jam(n, j)
					for jam in jams:
						fo.write('{} {}\n'.format(jam[0], jam[1]))


	def generate_jam(self, n, j):
		jam = [1] + [0] * (n - 2) + [1]
		res = []
		while len(res) < j:
			self.next_jam(jam)
			valid, divisors = self.is_valid_jam(jam)
			if valid:
				jam_string = ''.join(map(lambda x: str(x), jam))
				divisors_string = ' '.join(map(lambda x: str(x), divisors))
				res.append((jam_string, divisors_string))

		return res

	def next_jam(self, jam):
		for i in range(len(jam) - 2, 0, -1):
			if jam[i] == 0:
				jam[i] = 1
				for j in range(i + 1, len(jam) - 1):
					jam[j] = 0
				return


	def is_valid_jam(self, num):
		divisors = []

		for i in range(2, 11):
			num_in_base = self.convert(num, i)
			prime, divisor = self.is_prime(num_in_base)

			if prime:
				return (False, [])
			else:
				divisors.append(divisor)
		return (True, divisors)

	def convert(self, num, base):
		res = 0
		for i, x in enumerate(reversed(num)):
			res += (x * (base ** i))
		return res

	def is_prime(self, num):
		if num == 2:
			return (True, None)
		elif num % 2 == 0:
			return (False, 2)

		limit = ceil(sqrt(num))
		
		for i in range(3, limit, 2):
			if num % i == 0:
				return (False, i)

		return (True, None)

Jamcoin('C-small-attempt0.in', 'out.txt')