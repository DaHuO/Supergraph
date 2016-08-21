class Word:

	def __init__(self):
		self.s = ''

	def add(self, c):
		if self.s == '':
			self.s += c
		else:
			new_1 = c + self.s
			new_2 = self.s + c
			for i in xrange(len(new_1)):
				if ord(new_1[i]) > ord(new_2[i]):
					self.s = new_1
					return
				if ord(new_1[i]) < ord(new_2[i]):
					self.s = new_2
					return
			self.s = new_1

	def __str__(self):
		return self.s

with open('A-large.in', 'r') as f:
	test_cases = int(f.readline())
	for test_case in xrange(1, test_cases + 1):
		test_s = f.readline().strip()
		word = Word()
		for c in test_s:
			word.add(c)
		print 'Case #' + str(test_case) + ': ' + str(word)
