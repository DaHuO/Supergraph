class BleatrixSleepHelper:

	numbers = [i for i in xrange(10)]
	line_number = 0
	number_of_test_cases = 0
	numbers_remembered = []

	def check_limit(self, number):
		if number >= 0 and number <=10**6:
			return True
		else:
			return False

	def get_input_values(self, value):
		
		try:
			number = int(value)
		except ValueError:
			print "Invalid number"
			exit()
	
		if self.check_limit(number):
			pass
		else:
			print "Keep it upto 1000000"
			exit()
	

		if self.line_number == 0:
			
			if number >= 0 and type(number) == int:
				self.number_of_test_cases = number
				return number, True
		else:

			return number, False	
			

	def check_sleepy(self):

		self.numbers_remembered = sorted(self.numbers_remembered, key=int)
		if self.numbers_remembered == self.numbers:
			return True
		else:
			return False

	def get_sleeping_number(self, line_value):

		number, first_line = self.get_input_values(line_value)

		sleepy = False
		if first_line:
			pass
		else:
			sleepy_number = 0
			i = 0
			while(not sleepy):
				next_num = (i+1) * number
				if next_num == next_num * (i+2):
					this_line_number = self.line_number
					self.line_number += 1
					return "Case #{0}: INSOMNIA\n".format(this_line_number)

				t_nums = map(int, str(next_num))
				for t_n in t_nums:
					if t_n not in self.numbers_remembered:
						self.numbers_remembered.append(t_n)
				sleepy_yet = self.check_sleepy()
				if not sleepy_yet:
					i += 1
					continue
				else:
					sleepy_number = next_num
					sleepy = True
					break
			this_line_number = self.line_number
			self.line_number += 1
			return "Case #{0}: {1}\n".format(this_line_number, next_num)

def main():
	f = open('A-large.in', 'r')
	fw = open('output-2', 'w+')
	blea = BleatrixSleepHelper()
	blea.get_sleeping_number(f.readline())

	blea.line_number += 1
	while(blea.line_number <= blea.number_of_test_cases):
		blea.numbers_remembered = []
		crackin_number = blea.get_sleeping_number(f.readline())
		fw.write(crackin_number)


if __name__ == "__main__":
	main()


