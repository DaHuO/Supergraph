"""
Created on 2016/04/09

@author: nico
"""

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
    
    
def check_presence(string, character, start):
    presence = False
    index = -1
    
    for i in range(start, len(string)):
        if string[i] != character:
            break
        else:
            presence = True
            index = i
            
#    print character, start, presence, index
        
    return presence, index
        
    
    
 
def check_pancake_state(current_test, index_fixed, pancake_state):
    negative_presence, negative_index = check_presence(current_test, '-', index_fixed + 1)
    
    if pancake_state == 'S0':        
        if negative_presence:
            return 'S1', 1, negative_index
        else:
            positive_presence, positive_index = check_presence(current_test, '+', 0)
            return 'S1', 0, positive_index
    else:        
        if negative_presence:
            return 'S1', 2, negative_index
        else:
            positive_presence, positive_index = check_presence(current_test, '+', index_fixed + 1)
            return 'S1', 0, positive_index  
        


def solve_pancakes(current_test):
    index_fixed = -1
    pancake_state = 'S0'
    inversions = 0
    
    while pancake_state != 'S3':
#        print inversions, index_fixed, pancake_state
#        print '------------'
        pancake_state, partial_inversions, index_fixed = check_pancake_state(current_test, index_fixed, pancake_state)
        inversions += partial_inversions
#        print 'index_fixed: ' + str(index_fixed)
        
        if index_fixed == len(current_test) - 1:
            pancake_state = 'S3'           
        
    return inversions

   
    
    
    
input_lines = read_lines('input.txt')
input_lines = clean_up(input_lines)    



T_str = input_lines[0]
T = int(T_str)

solutions = []


for i in range(1, len(input_lines)):
    current_test = input_lines[i]
    current_solution = solve_pancakes(current_test)
    solutions.append(current_solution)
    
#print solutions


label = 'Case #'
output = ''

for i in range(0, len(solutions) - 1):
    index_output = i + 1
    output += label + str(index_output) + ': ' + str(solutions[i]) + '\n'
    
output += label + str(len(solutions)) + ': ' + str(solutions[len(solutions) - 1])
    
    
f = open("output.txt", "w")
f.write(output)
f.close()
    










