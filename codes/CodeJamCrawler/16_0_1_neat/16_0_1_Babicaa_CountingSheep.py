import sys

__author__ = 'andrej.babic@ringlspil.com'

with open(sys.argv[1]) as input_file:
    with open(sys.argv[2], "w") as output_file:
        number_of_examples = int(input_file.readline())

        for case_number in xrange(1, number_of_examples+1):
            N = int(input_file.readline())
            # The only way we don't get all the digits is if we have N as zero.
            if N == 0:
                output_file.write("Case #%d: INSOMNIA\n" % case_number)
                continue

            def find_digits(N):
                # Initialize the array for flagging digits and the counter.
                digits_flags = [False, False, False, False, False, False, False, False, False, False]
                digits_counter = 10

                last_number = N
                while True:
                    digits = str(last_number)
                    for digit in (ord(digit)-48 for digit in digits):
                        # Check if the digit is a new one. And check if we found all digits.
                        if not digits_flags[digit]:
                            digits_flags[digit] = True
                            digits_counter -= 1
                            if digits_counter == 0:
                                return last_number

                    last_number += N

            result = find_digits(N)
            output_file.write("Case #%d: %d\n" % (case_number, result))
