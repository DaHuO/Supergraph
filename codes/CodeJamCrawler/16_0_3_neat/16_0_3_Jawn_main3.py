import math

#Massively improved this code by just skipping over large number! Holy crap!

#prepare to fight
def read_file(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip('\n') for x in data]

    number1 = 0
    number2 = 0
    test_cases = int(data[0])
    sum_of_cases = []
    for test_cases in range(0,test_cases):
        temp = data[test_cases + 1]
        for i in range(len(temp)):
            if temp[i] == ' ':
                number1 = int(temp[:i])
                number2 = int(temp[i+1:])
        sum_of_cases.append([number1, number2])

    return sum_of_cases

#edit this statement
god_cases = read_file('C-large.in')


def convert_to_base_10(number):
    str_number = str(number)
    base_counter = 2
    power_counter = 0
    total = 0
    return_args = []
    while base_counter <= 10:
        for x in reversed(range(len(str_number))):
            temp = int(str_number[x]) * (base_counter ** power_counter)
            total = total + temp
            power_counter = power_counter + 1

        return_args.append(total)
        total = 0
        power_counter = 0
        base_counter = base_counter + 1

    return return_args

#I have to edit this function because stack overflow error for c-large
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
        if divisor >= 100000:
            return True
    return True

def prime_checker(num_list):
    return_list = []
    for x in range(len(num_list)):
        temp = is_prime(num_list[x])
        if temp == True:
            return_list.append('PRIME')
        else:
            return_list.append(temp)

    return return_list

def coin_jam(cases):
    return_list = []
    for x in range(len(cases)):
        to_return = []
        length = int((cases[x][0])) - 2
        num_created = cases[x][1]
        new_int = 0
        new_int2 = "{0:b}".format(new_int)

        while len(new_int2) <= length:
            if len(to_return) == int(num_created):
                break
            num_zeroes = length - int(len(new_int2))
            int_tester = '0'*num_zeroes
            int_tester = ''.join([int_tester,new_int2])

            #magic happens here.
            int_tester = ''.join(['1',int_tester,'1'])
            int_tester = int(int_tester)
            is_it_a_coin = prime_checker(convert_to_base_10(int_tester))
            for i in range(len(is_it_a_coin)):
                if is_it_a_coin[i] == 'PRIME':
                    break
                elif i + 1 == len(is_it_a_coin):
                    is_it_a_coin = [int_tester] + is_it_a_coin
                    to_return.append(is_it_a_coin)

            new_int = new_int + 1
            new_int2 = "{0:b}".format(new_int)

        if len(to_return) < int(num_created):
            return 'Google did not tell me what to put in if the jam coin is impossible.'
        else:
            return_list.append(to_return)
            to_return = []

    return return_list

#test your might
def write_file(file, to_return):
    new_str = ''
    with open(file, 'r+') as f:
        f.write('Case #' + str(len(god_cases)) + ':' + '\n')
        for i in range(len(to_return)):
            for x in range(len(to_return[i])):
                for z in range(len(to_return[i][x])):
                    if z != 0:
                        new_str = ' '.join([new_str, str(to_return[i][x][z])])
                    else:
                        new_str = ''.join([new_str, str(to_return[i][x][z])])

                f.write(new_str + '\n')
                new_str = ''
                '''if z != (len(to_return) - 1):
                    temp = str(to_return[i][x][z])
                    f.write(temp + '\n')
                else:
                    f.write(str(to_return[i][x][z]))'''

    #return file[0]

#edit this statement
write_file('output.in', coin_jam(god_cases))