len_input = int(raw_input())


def all_set(l):
	count = 0
	for i in l:
		count += i
	if count == 10:
		return True
	else:
		return False
def simulate_count(N):
	if N == 0:
		return "INSOMNIA"
	else:
		iteration = 0
		seen_digit = []
		for i in range(10):
			seen_digit.append(0)

		curr_n = N
		while not all_set(seen_digit):
			iteration += 1
			curr_n = N*iteration
			# print seen_digit
			digit_n = curr_n
			# print digit_n,"digit"
			while digit_n:
				digit = digit_n % 10
				digit_n = digit_n / 10
				seen_digit[digit] = 1

	return curr_n

def print_output(answer,index):
	print "Case #{0}: {1}".format(index,answer)

for case_num in range(len_input):
	_input = int(raw_input())
	sleep_count = simulate_count(_input)
	print_output(sleep_count,case_num+1)
