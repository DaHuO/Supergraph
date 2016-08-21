import sys


def check_pos(myString):
	flag = False
	for temp in myString:
		if temp == '+':
			flag = True
		else:
			flag = False
			break
	return flag

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	n = n[0]

	output = 0
	# print n
	while (not check_pos(n)):
		# print "inside while loop"
		index = -1
		for each_char in n:
			if each_char == n[0]:
				index = index + 1
			else:
				break;

		# print "im here now"
		# print n[0]
		if n[0] == '+':
			# print "in plus sign"
			reverse = '-'
		else:
			# print "in -ve sign"
			reverse = '+'
		# print "im here now 2"
		temp_list = list(n)
		for x in xrange(0,index+1):
			# print "inside this loop",x
			# sys.exit()
			temp_list[x] = reverse
		n = "".join(temp_list)
		# print n
		# sys.exit()
		output = output + 1

	print "Case #{}: {}".format(i, output)
	# sys.exit()

