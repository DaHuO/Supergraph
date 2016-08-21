input_file = open('B-large.in', 'r')
output_file = open('output.txt', 'w')
line_number = 0


T = int(input_file.readline())

for line in input_file:
    line_number += 1
    counter = 0

    if line_number == T:
        pancake_array = list(line[::-1])
    else:
        pancake_array = list(line[:-1][::-1])
    s_len = len(pancake_array)
    print pancake_array

    for i in xrange(0,s_len):
        current_char = pancake_array[i]
        if current_char == '-':
            counter += 1
            # flip maneuver
            for j in xrange(i,s_len):
                if pancake_array[j] == '-':
                    pancake_array[j] = '+'
                else:
                    pancake_array[j] = '-'
    output_line = 'Case #%s: %s'%(str(line_number),str(counter))
                
                
            
            

 #   output_line = 'Case #%s: %s'%(str(line_number),str(number))

    if line_number == T:
        output_file.write(output_line)
        print "Done"
    else:
        output_file.write(output_line + '\n')

input_file.close()
output_file.close()


