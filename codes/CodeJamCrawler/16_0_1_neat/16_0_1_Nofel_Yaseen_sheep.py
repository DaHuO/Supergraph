# import sys

def find_last(original):
	check = [False] * 10
	flag = True
	count = 0
	while(flag):
		count = count + 1
		input_num = original*count
		current = str(input_num)
		# print current
		for c in current:
			val = ord(c) - 48
			# print val
			if val >= 0 and val < 10:
				check[val] = True
		for item in check:
			if item is True:
				flag = False
			else:
				flag = True
				break
	return input_num
	# sys.exit()

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	n = n[0]
	# sys.exit()
	if n == 0:
		output = "INSOMNIA"
	else:
		output = find_last(n)
	print "Case #{}: {}".format(i, output)
	# check out .format's specification for more formatting options

# lines = [line.rstrip('\n') for line in open('test.txt')]

# print lines

# testCases = int(lines[0])
# print testCases

# lines.pop(0)

# print lines

# case = 0

# for line in lines:
# 	input_num = int(line)
# 	if (input_num == 0):
# 		case = case + 1
# 		print "Case #" , case, ": INSOMNIA"
# 	else:
# 		case = case + 1
# 		find_last(input_num,case)