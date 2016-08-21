class CountingSheep:
	def __init__(self, file_in, file_out):
		with open(file_in, 'r') as fi:
			with open(file_out, 'w') as fo:
				num_cases = int(fi.readline())

				for i in range(1, num_cases + 1):
					n = int(fi.readline())
					digit_set = set()
					curr_num = n

					if curr_num != 0:
						while not self.update_digit_set(curr_num, digit_set):
							curr_num += n
					else:
						curr_num = 'INSOMNIA'

					fo.write('Case #{}: {}\n'.format(i, curr_num))

	def update_digit_set(self, number, digit_set):
		while number > 0:
			last_digit = number % 10
			if last_digit not in digit_set:
				digit_set.add(last_digit)
			number = number // 10

		return len(digit_set) == 10

CountingSheep('A-large.in', 'out_lg.txt')