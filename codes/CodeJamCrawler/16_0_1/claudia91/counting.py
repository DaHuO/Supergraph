'''
Created on 09 apr 2016

@author: claudia91
'''
from common import test_case

def solve_problem(test_case):
    i = 1
    ls_num = []
    number = ''
    if test_case == 0:
        return 'INSOMNIA'
    while len(ls_num) < 10:
        number = str(i*test_case)
        for single_number in number:
            if single_number not in ls_num:
                ls_num.append(single_number)  
        i+=1
       
    return int(number)

def solve(data):
    return solve_problem(int(data[0]))
#open Output file
output = open(test_case.OUTPUT_FILE, 'w')
#read lines from input file
lines = test_case.read_file(test_case.INPUT_FILE)
for line in range(1, len(lines)):
    test_case.print_result(line, solve([lines[line]]), output)
# print solve_problem(0)
# print solve_problem(1)
# print solve_problem(2)
# print solve_problem(11)
# print solve_problem(1692)
