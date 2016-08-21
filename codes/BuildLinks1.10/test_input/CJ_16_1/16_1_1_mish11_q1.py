# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 5:29:09 2016

@author: M
"""
import string
abc_rev_upper = string.ascii_uppercase[::-1]

def get_best_word(original_word):
    new_string = ''    
    for char in original_word:
        if new_string is '':
            new_string += char
        else:
            if new_string[0]<=char:
                new_string = char + new_string
            else:
                new_string = new_string + char
    return new_string


input_path = r'C:\Users\M\Documents\Python\ocde jam 2016\1A\q1\A-large (2).in'
output_path = r'C:\Users\M\Documents\Python\ocde jam 2016\1A\q1\A_large.out'

input_file = open(input_path,'r')
output_file = open(output_path,'w')


num_cases = int(input_file.readline())
case_num = 1
for original_word in input_file:
    best_word =  get_best_word(original_word[:-1])
    print 'Case #' + str(case_num) + ': ' + str(best_word) + '\n'
    output_file.write('Case #' + str(case_num) + ': ' + str(best_word) + '\n')
    case_num +=1

input_file.close()
output_file.close()
