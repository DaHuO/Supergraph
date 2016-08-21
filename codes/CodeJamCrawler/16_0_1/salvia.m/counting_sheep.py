digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def read_file(filename):
    with open(filename, encoding="utf-8") as a_file:
        list_lines = []
        for line in a_file:
            line = line.strip()
            list_lines.append(line)

    return list_lines


file_list = read_file('A-large.in')    # change file here <<<-------------------------------------------
# print(file_list)

test_cases = int(file_list[0])
numbers = file_list[1:] # all numbers B will choose in list
to_print = []
for case in range(test_cases):
    lst_check = []
    check_d = []
    lst_check.append(numbers[case])
    # print(lst_check)
    if lst_check[0] == '0':
        to_print.append('INSOMNIA')
    i = 3
    while check_d != digits:
        if lst_check[0] == '0':
            break
        for el in range(2, i):
            lst_check.append(int(lst_check[0]) * el)

        for e in lst_check:   # adding digits to check how many different we have got
            for every_num in str(e):
                if every_num not in check_d:
                    check_d.append(every_num)
                    check_d.sort()
        if check_d == digits:
            to_print.append((lst_check[-1]))
            break
        else:
            i += 1

ans = []
for l in range(len(to_print)):
    ans.append("Case #" + str(l+1) + ": " + str(to_print[l]))

f = open('A-large-att', 'w')
for i in ans:
    f.write(i)
    f.write('\n')
f.close()
