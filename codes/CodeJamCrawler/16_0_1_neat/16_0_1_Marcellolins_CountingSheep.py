def extract_numbers(number):
	numbers = []

	number = str(number)

	for character in str(number.strip()):
		numbers.append(int(character))

	return numbers

def found_all_digits(numbers):
	for x in range(0,10):
			if x not in numbers:
				return False

	return True

def add_distinct_to_set(digits, hashset):
	for n in digits:
		if n not in hashset:
			hashset.add(n)

def write_to_output(output_value, test_case_index, f_writer):
	output_template = 'Case #%d: %s\n'

	output_value = str(output_value)

	f_writer.write(output_template % (test_case_index, output_value))

# File Handling
with open('Inputs/A-large.in', 'r') as f_reader:
	with open('Outputs/A-large.out' ,'w') as f_writer:

		# Test Cases
		test_cases = int(f_reader.readline())
		print 'Tests : %d' % test_cases

		# Iterating over file
		current_test = 1
		while current_test <= test_cases:
			
			# Reading Test Value
			input = f_reader.readline().strip()

			print '\tInput : %s' % input

			# ZERO MEANS IMNSONIA
			if input == '0':
				write_to_output('INSOMNIA', current_test, f_writer)
				print 'INSOMNIA'
				current_test = current_test + 1
				continue

			# Distinct digits
			seen_numbers = set()

			# Extracting digits of the first input
			tmp_numbers = extract_numbers(input)

			# Adding distinct numbers to set
			for x in tmp_numbers:
				if x not in seen_numbers:
					seen_numbers.add(x)
			
			# Loop Logic
			should_break = False
			current_multiplier = 2
			while not found_all_digits(seen_numbers):
				current_number = int(input) * current_multiplier
				
				# Extracting digits
				tmp_digits = extract_numbers(current_number)

				# Adding digits to hashset
				add_distinct_to_set(tmp_digits, seen_numbers)
				print seen_numbers

				# Test Index and Multiplier
				current_multiplier = current_multiplier + 1				

			write_to_output(current_number, current_test, f_writer)	
			current_test = current_test + 1
