input_file = open('A-large.in', 'r')
output_file = open('output.txt', 'w')
line_number = 0

T = int(input_file.readline())
for line in input_file:
    digits = {0,1,2,3,4,5,6,7,8,9}
    count = 1
    line_number += 1
    start_number =  int(line[:-1])
    if start_number == 0:
        output_line= 'Case #%s: INSOMNIA'%(str(line_number))
    else:
        while len(digits) > 0:
            number = str(start_number * count)
            for i in number:
                digits.discard(int(i))
            count += 1
        output_line = 'Case #%s: %s'%(str(line_number),str(number))
    if line_number == T:
        output_file.write(output_line)
        print "Done"
    else:
        output_file.write(output_line + '\n')

input_file.close()
output_file.close()
