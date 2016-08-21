fp_in = open('B-large.in', 'r')
fp_out = open('qual-B-largeout.txt', 'w')

def process_case(case):
	case = case.strip()
	end_index = -1
	flips = 0
	while True:
		end_index = end_index_first_subsequence(case)
		if end_index == len(case):
			return flips if case[0] == '+' else flips + 1
		case = flip_until(case, end_index)
		flips += 1

def flip_until(case, index):
	start_char = case[0]
	start_sequence = ''.join([('+' if start_char == '-' else '-') for x in range(0, index)])
	return start_sequence + case[index:]

def end_index_first_subsequence(case):
	sequence_start = case[0]
	for i, char in enumerate(case):
		if char != sequence_start:
			return i
	return len(case)

case_num = 1
cases = fp_in.readlines()
for case in cases[1:]:
	output_str = "Case #{0}: {1}\n".format(case_num, process_case(case))
	fp_out.write(output_str)
	case_num = case_num + 1
fp_in.close()
fp_out.close()
