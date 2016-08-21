file = open('A-large.in')
input_times = int(file.readline())

for i in range(input_times):
	case_input = int(file.readline())
	case_output = "INSOMNIA"
	if case_input == 0:
		pass
	else:
		digits = []
		case_round = 1

		while len(digits) < 10:
			case_output = str(case_round * case_input)
			for c in str(case_round * case_input):
				if not c in digits:
					digits.append(c)
			case_round = 1 + case_round

	print "Case #"+str(i+1)+": "+case_output
		

			
