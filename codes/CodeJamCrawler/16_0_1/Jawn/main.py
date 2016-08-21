
#prepare to fight
def read_file(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip('\n') for x in data]

    test_cases = int(data[0])
    sum_of_cases = []
    for test_cases in range(0,test_cases):
        sum_of_cases.append(data[test_cases + 1])

    return sum_of_cases

#edit this statement
god_cases = read_file('A-large.in')

#your function goes here
def sheep(cases):
    return_cases = []
    for i in range(len(cases)):
        number_list = []
        count_var = 1
        while True:
            if len(number_list) == 10:
                return_cases.append('Case #' + str(len(return_cases) + 1) + ': ' + str((count_var - 1) * int(cases[i])))
                count_var = 1
                break
            if count_var >= 1000000:
                return_cases.append('Case #' + str(len(return_cases) + 1) + ': INSOMNIA')
                count_var = 1
                break
            temp_var = int(cases[i]) * int(count_var)
            temp_var2 = str(temp_var)
            for y in range(len(temp_var2)):
                if temp_var2[y] not in number_list:
                    number_list.append(temp_var2[y])


            count_var = count_var + 1
    return return_cases



#test your might
def write_file(file, to_return):
    with open(file, 'r+') as f:
        for i in range(len(to_return)):
            if i != (len(to_return) - 1):
                f.write(to_return[i] + '\n')
            else:
                f.write(to_return[i])

    return file[0]

#edit this statement
write_file('output.in', sheep(god_cases))