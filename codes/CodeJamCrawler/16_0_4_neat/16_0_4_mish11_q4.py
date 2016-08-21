# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 17:57:09 2016

@author: M
"""

def get_attempts(first_gen_len, num_gen, num_attempts):
    if (num_attempts<first_gen_len-1) or (num_gen==1 and num_attempts !=first_gen_len):
        return 'IMPOSSIBLE'
    elif num_gen==1:
        attempts_arr = range(1,num_attempts+1)
    elif first_gen_len == 1:
        return 1
    else:
        attempts_arr = []
        for i in xrange(1,num_attempts):
            block_length = first_gen_len**(num_gen-1)
            cur_cell = block_length*(i-1) + i+1
            attempts_arr.append(cur_cell)
    return str(attempts_arr)[1:-1].replace(',','').replace('L','')


input_path = r'C:\Users\M\Documents\Python\ocde jam 2016\q4\D-small-attempt1.in'
output_path = r'C:\Users\M\Documents\Python\ocde jam 2016\q4\D_small2.out'

input_file = open(input_path,'r')
output_file = open(output_path,'w')


num_cases = int(input_file.readline())
case_num = 1
for line in input_file:
    split_line = line.split()
    first_gen_len = int(split_line[0])
    num_gen = int(split_line[1])
    num_attempts = int(split_line[2])

    print first_gen_len, num_gen, num_attempts
    
    attempts =  get_attempts(first_gen_len, num_gen, num_attempts)
    print 'Case #' + str(case_num) + ': ' + str(attempts) + '\n'
    output_file.write('Case #' + str(case_num) + ': ' + str(attempts) + '\n')
    case_num +=1

input_file.close()
output_file.close()