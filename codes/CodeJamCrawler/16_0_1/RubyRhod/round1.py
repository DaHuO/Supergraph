import sys
import os

def check_num(n,num_string,digits):
    num_check = int(num_string) * n
    num_check = str(num_check)
    if num_string == '0':
        return "INSOMNIA"
    for ch in num_check:
        ch = int(ch)
        if ch in digits:
            digits.remove(int(ch))
    if len(digits) == 0:
        return num_check
    return check_num(n+1,num_string,digits)

file_name = sys.argv[1]
file_out = open('output.txt','w')
first_line = False
digits = None
line_num = 0
with open(file_name) as fp:
    for line in fp:
        if line_num != 0:
            digits = list(range(10))
            line = line.strip()
            output = check_num(1,line,digits)
            file_out.writelines('Case #{0}: {1}\n'.format(line_num,output))
            line_num = line_num + 1
        else:
            line_num = line_num + 1


#codejam round 1




def print_output(output):
    pass
