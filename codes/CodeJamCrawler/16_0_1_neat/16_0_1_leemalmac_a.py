# Google Code Jam Qualification Round 2016
# Problem A. Counting Sheep
# Author: Nodari Lipartiya <nodari.lipartiya@gmail.com>

line_number = 1
num_of_test_cases = 0
case = 1


with open('A-large.in') as input_file, open('output_a_large.out', 'w+') as output_file:
    for line in input_file.readlines():
        if line_number == 1:
            num_of_test_cases = int(line)
            line_number += 1
            continue
        else:
            curr_num = int(line)

        if curr_num == 0:
            output_file.write("Case #{}: {}\n".format(case, 'INSOMNIA'))
            case += 1
            continue

        digits = {}
        multiplier = 0

        while multiplier <= 1000000:
            multiplier += 1
            num = str(curr_num*multiplier)

            for digit in num:
                if not digit in digits:
                    digits[digit] = True

            if len(digits.keys()) == 10:
                if case == num_of_test_cases:
                    output_file.write("Case #{}: {}".format(case, num))
                else:
                    output_file.write("Case #{}: {}\n".format(case, num))
                break

        case+=1
