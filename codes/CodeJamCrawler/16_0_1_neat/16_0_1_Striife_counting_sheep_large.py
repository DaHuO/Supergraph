
input_file = open('large_set.txt', 'r')     # Open file
output_file = open('result_large.txt', 'w')

for i, line in enumerate(input_file):     # read file by line
    start_number = int(line)
    
    if i == 0:                              # first line sets number of cases
        number_of_cases = int(line)
        case_number = 1
        
    else:                                   # if not first line, start
        start_number = int(line)
        print(start_number)
        if start_number == 0:
            out_string = "Case #%d: INSOMNIA\n" % (case_number)
            output_file.write(out_string)
            case_number = case_number + 1
            continue
        
        number_list = [0,1,2,3,4,5,6,7,8,9] # list of digits 
        multiplier = 1                      # sets the multiplier count, increments by 1
        
        while len(number_list) != 0:        # while number_list is not empty
            number_multi = start_number * multiplier
            print(number_multi, " : ", multiplier)
            number_string =  str(number_multi)
            
            for check_int in range(0,len(number_string)):
                print(check_int)
                
                for scratch_int in number_list:
                    
                    if int(number_string[check_int]) == scratch_int:
                        print(number_list)
                        number_list.remove(scratch_int)
                
            
            multiplier = multiplier + 1
        print(number_multi)
        out_string = "Case #%d: %d\n" % (case_number, number_multi)
        output_file.write(out_string)
        case_number = case_number + 1
        
input_file.close()