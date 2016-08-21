class Pancake:
	def __init__(self, file_in, file_out):
		with open(file_in, 'r') as fi:
			with open(file_out, 'w') as fo:
				num_cases = int(fi.readline())

				for i in range(1, num_cases + 1):
					arrangement = list(fi.readline())
					if arrangement[-1] == '\n':
						arrangement.pop()

					res = self.process(arrangement)
					fo.write('Case #{}: {}\n'.format(i, res))

	def process(self, arrangement):
		flips = 0
		while not self.all_smiley_up(arrangement):
			self.flip(arrangement)
			flips += 1

		return flips

	def flip(self, arrangement):
		# Edge case
		if len(arrangement) == 1:
			arrangement[0] = '+'
			return

		# Normal case
		pos = len(arrangement)
		for i in range(len(arrangement) - 1):
			if arrangement[i] != arrangement[i + 1]:
				pos = i + 1
				break
		
		flipped = arrangement[:pos]
		flipped.reverse()

		for i in range(pos):
			if flipped[i] == '+':
				arrangement[i] = '-'
			else:
				arrangement[i] = '+'



	def all_smiley_up(self, arrangement):
		for i in arrangement:
			if i == '-':
				return False
		return True

Pancake('B-large.in', 'out-lg.txt')