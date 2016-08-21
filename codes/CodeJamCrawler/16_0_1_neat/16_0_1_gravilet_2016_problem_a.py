v_dir = "k:\\Python\\codejam\\2016_problem_a\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1

while v_test_number <= v_number_of_tests:
    v_first_number = int(v_txt_in.readline())
    v_number = 0
    c = []

    while (len(c) < 10 and v_first_number != 0):
        v_number += v_first_number
        c.extend(list(str(v_number)))   # add digits from new number
        c = list(set(c))                # delete dublicates
#        c.sort()
#        print(v_number)
#        print(c)

#    print('==========')
    if v_first_number != 0:
        v_txt_out.write("Case #" + str(v_test_number) + ": " + str(v_number) + "\n")
    else:
        v_txt_out.write("Case #" + str(v_test_number) + ": " + 'INSOMNIA' + "\n")
    v_test_number += 1

"""
    v_diners = v_txt_in.readline()
    info = v_txt_in.readline().split()
    arr = info
    print(arr)
    arr_feat = []
    for i in arr

    v_test_number += 1
"""

"""
for line in v_txt_in:
    # print(line)
    answer = 0
    position = 0
    sum = 0
    info = line.split()
    # print(info)
    # print(info[1])
    # for i in info[1] :
    # print(i)
    # print(int(info[0]),position)
    while position <= int(info[0]):
        if position > sum:
            answer += 1
            sum += 1
        sum += int(info[1][position])
        # print(int(info[1][position]), answer, sum)
        position += 1
    # print("case #",index_of_line,": ",answer, sep='')
    v_txt_out.write("case #"+str(index_of_line)+": "+str(answer)+"\n")
    v_index_of_line += 1
"""