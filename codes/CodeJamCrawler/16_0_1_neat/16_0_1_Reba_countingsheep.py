###
 # Google Code Jam
 # Author Rebecca Chen
###
 
input_file = open('A-large.in', 'r')
output_file = open('A-large.out', 'w')
 
num_cases = int(input_file.readline())
 
for i in range(num_cases):
    output_file.write('Case #' + str(i+1) + ': ')
     
    start_num = int(input_file.readline())
    if start_num == 0:
        output_file.write('INSOMNIA')
    else:
        digits = set()
        num = 0
        while len(digits) != 10:
            num += start_num
            for d in str(num):
                digits.add(d)
        output_file.write(str(num))

    output_file.write('\n')
     
input_file.close()
output_file.close()
