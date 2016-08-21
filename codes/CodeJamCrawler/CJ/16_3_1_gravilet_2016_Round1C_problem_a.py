v_dir = "k:\\Python\\codejam\\2016_Round1C_problem_a\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1
v_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while v_test_number <= v_number_of_tests:
    v_number_of_parties = int(v_txt_in.readline())
    v_line = v_txt_in.readline()
    info = list(map(int, v_line.split()))
    v_result_string = ''
    while sum(info) > 0:
        v_max = max(info)       # max element
        v_max_index = info.index(v_max) # Возвращает положение первого элемента (от start до end) со значением x
        print(v_abc[v_max_index])
        v_result_string = v_result_string + v_abc[v_max_index]
        info[v_max_index] = info[v_max_index] - 1
        if max(info) > sum(info)/2 :
            v_max = max(info)  # max element
            v_max_index = info.index(v_max)  # Возвращает положение первого элемента (от start до end) со значением x
            print('+++' + v_abc[v_max_index])
            v_result_string = v_result_string + v_abc[v_max_index]
            info[v_max_index] = info[v_max_index] - 1
        if max(info) > sum(info) / 2:
            print('!!!!!!!!!!!!!!')
        v_result_string = v_result_string + ' '
    print('======')

    v_txt_out.write("Case #" + str(v_test_number) + ": " + v_result_string + "\n")
    # v_txt_out.write("Case #" + str(v_test_number) + ": " + v_result_string)     # my v_result_string ALREADY have \n !!!
    v_test_number += 1

