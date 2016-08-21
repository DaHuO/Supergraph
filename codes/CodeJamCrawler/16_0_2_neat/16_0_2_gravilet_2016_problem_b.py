v_dir = "k:\\Python\\codejam\\2016_problem_b\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1

while v_test_number <= v_number_of_tests:
    v_line = v_txt_in.readline()
    v_line = v_line.rstrip()            # delete \n
    v_line = v_line + '+'               # it give +1 change of sign if last is '-'
    answer = 0
    v_symbol_previous = v_line[0]       # so the first symbol haven't changes of sign

    for symbol in v_line:               # the answer is number of change of sign (+1 if last is '-')
        if symbol != v_symbol_previous:
            answer += 1
        v_symbol_previous = symbol

    print(answer)
    v_txt_out.write("Case #" + str(v_test_number) + ": " + str(answer) + "\n")
    v_test_number += 1

