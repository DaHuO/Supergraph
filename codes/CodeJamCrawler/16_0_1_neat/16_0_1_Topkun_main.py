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