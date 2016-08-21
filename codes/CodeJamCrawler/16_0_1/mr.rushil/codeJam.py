import sys
input_data = sys.stdin.readlines()

num_cases = input_data[0]

for case in range(1, len(input_data)):
	seen_all_digits = False
	seen_field = [False]*10

	value = input_data[case].replace("\n", "").strip()
	if int(value) == 0:
		print "Case #"+str(case)+": INSOMNIA"
	else:
		number = value
		iteration = 1
		while seen_field.count(True) != len(seen_field):
			number = str(int(value) * iteration)
			for digit in number:
				seen_field[int(digit)] = True
			iteration = iteration + 1
		print("Case #"+str(case)+": "+number)
