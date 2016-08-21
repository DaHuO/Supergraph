# Read from the Code Jam Input file
with open("qualification1_counting_sheep_input.txt", "r") as open_file:
    with open("qualification1_counting_sheep_output.txt", "a+") as write_file:
        # Read input lines
        input_lines = [line.strip() for line in open_file.readlines()]
        # Now process; First accept the number of test cases
        n = int(input_lines[0].strip())
        # Now iterate over and run the function
        for _ in range(n):
            # Take in an input
            number = int(input_lines[1 + _].strip())
            # First keep track of all the digits
            digit_tracker = [0 for __ in range(10)]
            # Keep track of found
            found = False
            # Now go over an find the number
            for number_multiple in range(1, 1000):
                # Solve for the new number
                number_multiplied = number_multiple * number
                # Now, grab all its digits
                number_multiplied = list(str(number_multiplied))
                # Now fill in spots
                for digit in number_multiplied:
                    digit_tracker[int(digit)] = 1
                # I go over all digits in the Digit Tracker
                if len(list(filter(lambda x: x == 0, digit_tracker))) == 0:
                    # We found the number
                    print("CASE #" + str(_ + 1) + ":", ''.join(number_multiplied), file=write_file)
                    # Change found and exit
                    found = True
                    break
            # Check if found
            if not found:
                print("CASE #" + str(_ + 1) + ": INSOMNIA", file=write_file)
