
def solution():
	t = int(input())

	for i in range(t):
		n = input()
		output_str = "Case #{0}: {1}".format(*output_results(i, n))
		print(output_str)

def has_fallen_asleep(count_dict):
		for key in count_dict:
			if count_dict[key] < 1:
				return False
		return True

def output_results(case_num, case_input, max_count=10**6):
	digits = '1234567890'
	counts = [0,0,0,0,0,0,0,0,0,0]
	case_input = int(case_input)
	count_dict = dict(zip(digits, counts))
	last_val = None
	product = 0
	for count in range(1, max_count+1):
		product = str(case_input * count)
		for c in product:
			count_dict[c] += 1
		if has_fallen_asleep(count_dict):
			last_val = product
			break

	if last_val == None:
		return (case_num+1, 'INSOMNIA')
	else:
		return (case_num+1, last_val)

solution()