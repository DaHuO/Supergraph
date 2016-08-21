import os

input_file = open("input_large.in", "r")
output_file = open("output_large.txt", "w")

cases = int(input_file.readline())

for i in range(cases):
	N = long(input_file.readline())

	nums = []
	for j in range((2 * N) - 1):
		newline = input_file.readline()[:-1].split(" ")
		newline = [int(k) for k in newline]

		for num in newline:
			if num in nums:
				nums.remove(num)
			else:
				nums.append(num)

	nums.sort()
	nums = [str(num) for num in nums]
	answer = " ".join(nums)
		
	output_file.write("Case #" + str(i+1) + ": " + answer + "\n")