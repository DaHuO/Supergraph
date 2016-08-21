test = int(input())  # read a line with a single integer
for t in range(1, test + 1):
	k, c, s = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	print("Case #{}:".format(t), end = '')
	for i in range(1,k+1):
		print(" {}".format(i), end = '')
	print('')
