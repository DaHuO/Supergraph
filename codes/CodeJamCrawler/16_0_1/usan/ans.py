try:
	# open the file for reading
    input_file = open("A-large.in", 'r')
    output_file = open("A-large.out", 'w')

except IOError:
	print("Error reading or writing to file")
else:
    t = int(input_file.readline())
	# loop through the input
    for case_num in range(0, t):

        n = int(input_file.readline().rstrip())

        # initialize values
        i = 1
        unique_nums = set()
        unique_nums_len = 0
        insomnia = True

        # keep track of the number of times the unique numbers
        # set stayed at the same size
        times_same = 0

        while times_same < 1000000:
            # add the new unique numbers
            new_num = n * i
            unique_nums.update(str(new_num))

            # check if all digits present
            if len(unique_nums) == 10:
                insomnia = False
                biggest = new_num
                break

            if unique_nums_len == len(unique_nums):
                times_same += 1
            else:
                # reset the counter
                times_same = 0

            i += 1
            unique_nums_len = len(unique_nums)

        # write to file
        if insomnia:
            output_file.write("Case #" + str(case_num+1) + ": INSOMNIA\n")
        else:
            output_file.write("Case #" + str(case_num+1) + ": " + str(biggest) + "\n")

finally:
    input_file.close()
    output_file.close()