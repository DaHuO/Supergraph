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
god_cases = read_file('B-large.in')



def ham(cases):
    return_cases = []
    for z in range(len(cases)):
        data_pull = str(cases[z])
        temp_str = '+' * len(data_pull)
        temp_list = list(temp_str)
        runthrough = 0
        for i in reversed(range(len(data_pull))):
            if temp_list[i] != data_pull[i]:
                runthrough = runthrough + 1
                for x in range(len(temp_list)):
                    if x <= i:
                        if temp_list[x] == '+':
                            temp_list[x] = '-'
                        elif temp_list[x] == '-':
                            temp_list[x] = '+'
                        else:
                            print('You lied to me Google!')
        return_cases.append('Case #' + str(len(return_cases) + 1) + ': ' + str(runthrough))
    return return_cases


#print(ham(god_cases))


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
write_file('output.in', ham(god_cases))