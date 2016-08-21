dir = "./"
in_file = dir + "input_1.txt"

f_in = open(in_file)
output_name = "output_1.txt"
f_out = open(output_name, 'w')

number_of_tests = int(f_in.readline())

test_number = 1

while test_number <= number_of_tests:
    line = f_in.readline()
    line = line.rstrip()            # delete \n
    line = line + '+'               # it give +1 change of sign if last is '-'
    answer = 0
    prev_symb = line[0]       # so the first symbol haven't changes of sign

    for symbol in line:               # the answer is number of change of sign (+1 if last is '-')
        if symbol != prev_symb:
            answer += 1
        prev_symb = symbol

    f_out.write("Case #" + str(test_number) + ": " + str(answer) + "\n")
    test_number += 1

