fp_in = open('A-large.in', 'r')
fp_out = open('qual-a-largeout.txt', 'w')

def process_case(case):
	case = case.strip()
	n = int(case)
	if (n == 0):
		return 'INSOMNIA'
	counts = { str(x) : 0 for x in range(0,10) }
	m = 1
	while True:
		mn = n * m
		for digit in str(mn):
			counts[digit] = 1
		if sum(counts.itervalues()) == 10:
			return mn
		m += 1


case_num = 1
cases = fp_in.readlines()
for case in cases[1:]:
	output_str = "Case #{0}: {1}\n".format(case_num, process_case(case))
	# print(output_str)
	fp_out.write(output_str)
	case_num = case_num + 1
fp_in.close()
fp_out.close()
