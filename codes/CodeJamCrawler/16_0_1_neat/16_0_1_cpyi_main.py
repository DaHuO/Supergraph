# File name
input_file_name = "A-small-attempt0.in"
#input_file_name = "B-large.in"
#input_file_name = "small.txt"
output_file_name = input_file_name + '.out'

# Input input_file
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

# Total cases
case_number = int(input_file.readline())

# Deal with each case
for case_i in range(case_number):

    # Readin
    line = input_file.readline()
    start_number = int(line)

    found = []
    for i in range(10):
        found.append(False)

    multiplied_number = start_number

    if(start_number == 0):
        output_file.write('Case #' + str(case_i + 1) + ': INSOMNIA\n')
    else:
        while(1):
            finished = True
            for i in range(10):
                if(found[i] == False):
                    number_str = str(multiplied_number).strip()
                    for j in range(len(number_str)):
                        if(int(number_str[j]) == i):
                            found[i] = True
                if(found[i] == False):
                    finished = False
            if(finished == True):
                break
            else:
                multiplied_number = multiplied_number + start_number
        output_file.write('Case #' + str(case_i + 1) + ': ' + str(multiplied_number) + '\n')
        
input_file.close()
output_file.close()
