# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 13:29:09 2016

@author: M
"""

def get_num_flips(pancakes):
    num_flips = 0
    if pancakes[0] == '-':
        num_flips+= 1
    num_flips += pancakes.count('+-')*2
    return num_flips


input_path = r'C:\Users\M\Documents\Python\ocde jam 2016\q2\B-large.in'
output_path = r'C:\Users\M\Documents\Python\ocde jam 2016\q2\B_large.out'

input_file = open(input_path,'r')
output_file = open(output_path,'w')


num_cases = int(input_file.readline())
case_num = 1
for pancakes in input_file:
    num_flips =  get_num_flips(pancakes)
    print 'Case #' + str(case_num) + ': ' + str(num_flips) + '\n'
    output_file.write('Case #' + str(case_num) + ': ' + str(num_flips) + '\n')
    case_num +=1

input_file.close()
output_file.close()
