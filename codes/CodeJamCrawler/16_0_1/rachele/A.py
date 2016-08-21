input_file = "A-large.in"
output_file = "Alarge.out"

f_in = open(input_file, "r")
f_out = open(output_file, "w")

test_cases = int(f_in.readline()[:-1])

for case in range(test_cases):
	f_out.write("Case #" + str(case+1) + ": ")
	#print ("Case #" + str(case+1) + ": ")
	start = int(f_in.readline())

	if start == 0:
		f_out.write("INSOMNIA\n")
		#print ("INSOMNIA\n")
	else:
		nums = [0]*10
		uncovered = 10
		current = 0
		while uncovered > 0:
			current += start
			#print("current: "+str(current))
			for digit in str(current):
				if nums[int(digit)] == 0:
					nums[int(digit)] = 1
					uncovered -= 1
		f_out.write(str(current) + "\n")
		#print(str(current) + "\n")

f_in.close()
f_out.close()