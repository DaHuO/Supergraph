# File name
input_file_name = "D-small-attempt0.in"
output_file_name = input_file_name + '.out'

# Input input_file
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

# Total cases
case_number = int(input_file.readline())

# Deal with each case
for case_i in range(case_number):

    # Always do some formating after split
    line = input_file.readline()
    K = int(line.split(' ')[0])
    C = int(line.split(' ')[1])
    S = int(line.split(' ')[2])

    # Complexity = 1 is quite different
    if C == 1:
        # Output to file
        if(K > S):
            output_file.write('Case #' + str(case_i + 1) + ': IMPOSSIBLE' + '\n')
        else:
            output_file.write('Case #' + str(case_i + 1) + ':')
            for i in range(K):
                idx = i + 1
                output_file.write(' ' + str(idx))
            output_file.write('\n')
    else:
        # Calculate min student required
        if K % 2 == 0:
            student_min = K / 2
        else:
            student_min = K / 2 + 1

        # Possible or not
        if(student_min > S):
            output_file.write('Case #' + str(case_i + 1) + ': IMPOSSIBLE' + '\n')
        else:
            # Initialize the position
            pos = []
            for i in range(student_min):
                pos.append(i * 2)

            # Do position update
            for complexity_i in range(1, C):
                if(complexity_i == 1):
                    for pos_i in range(len(pos)):
                        pos[pos_i] = pos[pos_i] * K + (pos[pos_i] + 1)

                        # Last position may overflow
                        if(pos[pos_i] == K * K):
                            pos[pos_i] = pos[pos_i] - 1
                else:
                    for pos_i in range(len(pos)):
                        pos[pos_i] = pos[pos_i] * K

            # Output the result
            output_file.write('Case #' + str(case_i + 1) + ':')
            for pos_i in range(len(pos)):
                idx = pos[pos_i] + 1
                output_file.write(' ' + str(idx))
            output_file.write('\n')

input_file.close()
output_file.close()
