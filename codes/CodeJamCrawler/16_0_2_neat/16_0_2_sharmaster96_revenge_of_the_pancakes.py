def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('B-large.in', 'r'), open('B-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	pancake_stack = [c for c in in_file.readline() if c == '+' or c == '-']
	inversions = 0
	for i in range(1, len(pancake_stack)):
		if pancake_stack[i-1] != pancake_stack[i]:
			inversions = inversions + 1
	if pancake_stack[-1] == '-':
		inversions = inversions + 1
	epilogue(str(inversions), case_num)
