with open('input.txt', 'r') as f:
	with open('output.txt', 'w') as o:
		cases = int(f.readline())
		for case in range(cases):
			s = f.readline()
			#Count zeros
			numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
			num_zeros = s.count('Z')
			for character in numbers[0]:
				s = s.replace(character, '', num_zeros)
			num_four = s.count('U')
			for character in numbers[4]:
				s = s.replace(character, '', num_four)
			num_five = s.count('F')
			for character in numbers[5]:
				s = s.replace(character, '', num_five)
			num_two = s.count('W')
			for character in numbers[2]:
				s = s.replace(character, '', num_two)
			num_eight = s.count('G')
			for character in numbers[8]:
				s = s.replace(character, '', num_eight)
			num_six = s.count('X')
			for character in numbers[6]:
				s = s.replace(character, '', num_six)
			num_seven = s.count('V')
			for character in numbers[7]:
				s = s.replace(character, '', num_seven)
			num_three = s.count('H')
			for character in numbers[3]:
				s = s.replace(character, '', num_three)
			num_nine = s.count('I')
			for character in numbers[9]:
				s = s.replace(character, '', num_nine)
			num_one = s.count('O')
			for character in numbers[1]:
				s = s.replace(character, '', num_one)
			answer = '0' * num_zeros + '1' * num_one + '2' * num_two + '3' * num_three \
			 + '4' * num_four + '5' * num_five + '6' * num_six + '7' * num_seven + \
			 '8' * num_eight + '9' * num_nine
			o.write('Case #{}: {}\n'.format(case + 1, answer))