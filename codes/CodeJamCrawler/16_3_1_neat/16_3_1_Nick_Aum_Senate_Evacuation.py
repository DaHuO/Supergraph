"""
Created on 2016/05/08

@author: nico
"""

import string
import operator


def read_lines(path):
    f = open(path, 'r')
    all_lines = f.readlines()
    f.close()
    return all_lines



def clean_up(all_lines):
    final_lines = []
    
    for line in all_lines:
        line = line.replace('\n','')
        line = line.replace('\r','')
        final_lines.append(line)

    return final_lines
    
    

def solve_problem(parties_amount, senators_str):
    uuper_case_letters = string.ascii_uppercase
    solution = []
    senators_str_lst = senators_str.split()
    senators_lst = [int(i) for i in senators_str_lst]
    total_senators = sum(senators_lst)
    
    senators_party = []
    
    for i in range(len(senators_lst)):
        senators_party.append([senators_lst[i], uuper_case_letters[i]])        

    senators_party = sorted(senators_party, key=operator.itemgetter(0))
    
    while(total_senators > 0):
        way_out = senators_party[-1][1]
        total_senators -= 1
        senators_party[-1][0] = senators_party[-1][0] - 1
                
        if total_senators > 0:
            half_amount = (total_senators - 1)/2
            
            if senators_party[-1][0] == 0:
                    senators_party.pop()
                    
            senators_party = sorted(senators_party, key=operator.itemgetter(0))
                    
            if len(senators_party) == 1:
                way_out += senators_party[-1][1]
                total_senators -= 1
                senators_party[-1][0] = senators_party[-1][0] - 1                    
            elif senators_party[-1][0] - 1 <= half_amount and senators_party[-2][0] <= half_amount:
                way_out += senators_party[-1][1]
                total_senators -= 1
                senators_party[-1][0] = senators_party[-1][0] - 1             
                
        if total_senators > 0:                
            if senators_party[-1][0] == 0:
                senators_party.pop()                
            
            senators_party = sorted(senators_party, key=operator.itemgetter(0))
        
       
        solution.append(way_out) 
    
    str_solution = solution[0]

    for i in range(1, len(solution)):
        str_solution += ' ' + solution[i]       
    
    return str_solution
    

   

    
    
input_lines = read_lines('input.txt')
input_lines = clean_up(input_lines)    



T_str = input_lines[0]
T = int(T_str)

solutions = []


for i in range(1, len(input_lines), 2):
    current_parties = input_lines[i]
    current_senators = input_lines[i + 1]    
    current_solution = solve_problem(int(current_parties), current_senators)
    solutions.append(current_solution)
    
    
#print solutions
label = 'Case #'
output = ''

if solutions:
    for i in range(0, len(solutions) - 1):
        index_output = i + 1
        output += label + str(index_output) + ': ' + solutions[i] + '\n'
        
    output += label + str(len(solutions)) + ': ' + solutions[len(solutions) - 1]
    
   
f = open("output.txt", "w")
f.write(output)
f.close()


    










