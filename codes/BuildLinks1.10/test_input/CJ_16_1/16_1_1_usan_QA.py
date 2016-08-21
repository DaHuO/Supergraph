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

        s = input_file.readline().rstrip()
        output = s[0] # start with the first character

        for i in range(1, len(s)):
            ch = s[i]
            if ch >= output[0]:
                output = ch + output
            else:
                output += ch

        output_file.write("Case #" + str(case_num+1) + ": " + output + "\n")

finally:
    input_file.close()
    output_file.close()