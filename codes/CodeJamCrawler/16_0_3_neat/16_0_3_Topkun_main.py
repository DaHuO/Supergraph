import random


def problem_A():
    input = open('A-large.in','r')
    output = open('A-large.out','w')
    total_cases = input.readline().strip('\n')

    case_list = input.read().split('\n')
    case_no=1
    for each_case in case_list:
        start_number = int(each_case)
        multiplier = 1
        seen_count = []
        last_number = ''
        start_number
        while len(seen_count)<10:
            if start_number == 0:
                last_number = 'INSOMNIA'
                break
            current_number = start_number*multiplier
            for each_number in str(current_number):
                if each_number not in seen_count:
                    seen_count.append(each_number)
                    last_number = current_number
            multiplier +=1
        output.write('Case #' + str(case_no) + ': ' + str(last_number) + '\n')
        case_no+=1
def problem_B():
    input = open('B-large.in','r')
    output = open('B-large.out','w')
    case_count = input.readline()
    case_list = input.read().split('\n')
    case_no = 1
    for each_case in case_list:
        pancake_stack = list(each_case)
        to_flip_list = []
        current_side = ''
        flip_count = 0
        i=0
        while '-' in pancake_stack:
            if not to_flip_list:
                to_flip_list.append(i)
                current_side = pancake_stack[i]
            elif pancake_stack[i] == current_side:
                to_flip_list.append(i)
            if pancake_stack[i] != current_side or i == len(pancake_stack)-1:
                for each_i in to_flip_list:
                    if pancake_stack[each_i] == '+':
                        pancake_stack[each_i] = '-'
                    elif pancake_stack[each_i] == '-':
                        pancake_stack[each_i] = '+'
                to_flip_list = []
                flip_count += 1
                i=0
            else:
                i+=1
        output.write('Case #' + str(case_no) + ': ' + str(flip_count) + '\n')
        print 'Case #' + str(case_no) + ': ' + str(flip_count)
        case_no += 1
def problem_C():
    def is_valid(coin):
        if coin[0] == '1' and coin[-1] == '1':
            return True
        else:
            return False
    def not_prime(coin):
        base_list = [2,3,4,5,6,7,8,9,10]
        divider_list = []
        digit_list = list(coin)
        for each_base in base_list:
            value = 0
            for each_digit in range(0,len(digit_list)):
                value += int(digit_list[each_digit]) * pow(each_base,len(digit_list)-each_digit-1)

            divider = 2
            base_is_prime = True
            while divider < pow(pow(value,0.5),0.5):
                if value % divider == 0:
                    base_is_prime = False
                    divider_list.append(divider)
                    break
                else:
                    if divider == 2:
                        divider += 1
                    else:
                        divider += 2
            if base_is_prime:
                return False, []
            else:
                continue
        return True , divider_list
    def is_jamcoin(coin):
        if is_valid(coin):
            result,result_list = not_prime(coin)
            if result == True:
                return result_list
        return False
    #small case
    digit = 32
    sample = 50
    output = open('output','w')
    random_string = ''
    random_set = []
    sample_list = []
    while len(sample_list) < 500:
        while random_string=='' or random_string in random_set:
            random_string = ''
            for i in range(0,digit):
                random_string += str(random.randint(0,1))
        print random_string
        random_set.append(random_string)
        result = is_jamcoin(random_string)
        if result == False:
            continue
        else:
            sample_list.append([random_string, result])
            print len(sample_list)
    output.write('Case #1:' + '\n' )
    for each_sample in sample_list:
        output.write(each_sample[0] + ' ' + ''.join([str(x) + ' ' for x in each_sample[1]]) + '\n')

problem_C()