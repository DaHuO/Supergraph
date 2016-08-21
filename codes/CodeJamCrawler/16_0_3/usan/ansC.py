def get_factors(numbers):
    factors = []
    times_tried = 0
    for num in numbers:
        max_check = int(num**0.5) + 1 # sqrt n
        found = False

        # check for 2
        if (num % 2 == 0):
            found = True
            factors.append(2)
        else:
            # start looking for factors
            for f in range(3, max_check, 2):
                times_tried += 1 # keep track of how many attempts made
                if times_tried > 100: # move on
                    break
                if num % f == 0:
                    factors.append(f)
                    found = True
                    break

        # terminate if this was prime
        if not found:
            return False

    # if everything went well, return the factors
    return factors

try:
  # open the file for reading
    input_file = open("C-large.in", 'r')
    output_file = open("C-large.out", 'w')

except IOError:
  print("Error reading or writing to file")
else:
    # write to file
    output_file.write("Case #1:\n")

    t = int(input_file.readline())
    # loop through the input
    for case_num in range(0, t):
        line = input_file.readline().split(' ')
        n = int(line[0]) # length
        j = int(line[1]) # number of jamcoins

        format_string = '0' + str(n-2) + 'b'

        bin_counter = 0 # counter for bin represented in dec

        while j > 0:
            # get the next 'prospective' string
            string_test = "1" + format(bin_counter, format_string) + "1"

            # represent in different bases
            interpretations = [int(string_test, 2), int(string_test, 3),
                int(string_test, 4), int(string_test, 5), int(string_test, 6),
                int(string_test, 7), int(string_test, 8), int(string_test, 9),
                int(string_test, 10)]

            factors = get_factors(interpretations)

            # only write this string to the output if it was legit
            if factors:
                output_file.write(string_test + ' ' + ' '.join(map(str, factors)) + "\n")
                j -= 1

            # move on to next number
            bin_counter += 1


finally:
    input_file.close()
    output_file.close()
