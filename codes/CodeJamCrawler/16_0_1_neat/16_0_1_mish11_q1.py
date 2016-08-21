# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 12:42:22 2016

@author: M
"""

def get_last_num(first_num):
    if first_num == 0:
        return 'INSOMNIA'
    
    cur_num = first_num      
    num_arr = [0]*10
    while sum(num_arr)<10:
        for char in str(cur_num):
            num_arr[int(char)] = 1
        cur_num += first_num
    return cur_num - first_num


input_path = r'C:\Users\M\Documents\Python\ocde jam 2016\A-large.in'
output_path = r'C:\Users\M\Documents\Python\ocde jam 2016\A_large.out'

input_file = open(input_path,'r')
output_file = open(output_path,'w')


num_cases = int(input_file.readline())
case_num = 1
for line in input_file:
    first_num = int(line)
    last_num =  get_last_num(first_num)
#    print 'Case #' + str(case_num) + ': ' + str(last_num) + '\n'
    output_file.write('Case #' + str(case_num) + ': ' + str(last_num) + '\n')
    case_num +=1

input_file.close()
output_file.close()



    