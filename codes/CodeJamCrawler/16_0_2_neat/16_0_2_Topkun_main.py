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

problem_B()