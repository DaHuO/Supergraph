ALL_DIGIT_SET = set([0,1,2,3,4,5,6,7,8,9])

def extract_digits(num):
	if num == 0:
		return set([0])
	digits = set()
	while num > 0:
		digits.add(num%10)
		num = num//10
	return digits

def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	i = int(in_file.readline())
	if i == 0:
		epilogue("INSOMNIA", case_num)
		continue
	curr_val = i
	digits_seen = set()
	while True:
		print(curr_val)
		digits_seen = digits_seen.union(extract_digits(curr_val))
		if digits_seen == ALL_DIGIT_SET:
			break
		curr_val += i
	print()
	epilogue(str(curr_val), case_num)
