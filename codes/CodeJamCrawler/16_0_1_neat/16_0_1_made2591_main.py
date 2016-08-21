inputs = open("A-large.in.txt", "r").read().split("\n")
input_counter = 0
for input_ in inputs[1:-1]:
	input_orig = int(input_)
	founded_digit_for_input_ = []
	stop = False
	counter = 1
	if int(input_) == 0:
		print ("Case #%s: %s" % (input_counter+1, "INSOMNIA"))
	else:
		while not stop:
			stop = True
			input_ = int(input_orig) * counter
			for digit in str(input_):
				founded_digit_for_input_.append(int(digit))
				founded_digit_for_input_ = list(set(founded_digit_for_input_))
			for i in range(0, 10):
				if i not in founded_digit_for_input_:
					stop = False
			if stop:
				print ("Case #%s: %s" % (input_counter+1, input_))
			counter += 1
	input_counter += 1