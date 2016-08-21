v_dir = "k:\\Python\\codejam\\2016_problem_d\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

                                            # is primal

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1

while v_test_number <= v_number_of_tests:
    v_line = v_txt_in.readline()
    info = v_line.split()
    #print(info)
    v_K = int(info[0])
    v_C = int(info[1])
    v_S = int(info[2])
    print(str(v_K))
    print(str(v_C))
    print(str(v_S))
    print("====")

    if v_K == v_S:
        i = 1
        v_answer = "Case #" + str(v_test_number) + ": "
        while i <= v_S:
            v_answer += str(i) + " "
            i += 1

    v_txt_out.write(v_answer + "\n")

    v_test_number += 1

