import sys

n = int(raw_input())
nums = []

for i in range(n):
	nums = nums + [int(raw_input())]

for i, num in enumerate(nums):
	sys.stdout.write('Case #' + str(i+1) + ": ")

	if num == 0:
		sys.stdout.write("INSOMNIA\n")
		continue

	digits = {}
	orig_num = num
	num = 0
	while (len(digits) < 10):
		num = num + orig_num
		for d in str(num):
			digits[d] = True	

	sys.stdout.write(str(num) + "\n")
