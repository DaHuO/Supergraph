"""
Created on 2016/04/30

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
    
    
    
    

def solve_problem(input_item):
    digits = [0] * 10
    digits[0] = input_item.count('Z')
    digits[2] = input_item.count('W')
    digits[6] = input_item.count('X')
    digits[4] = input_item.count('U')
    digits[8] = input_item.count('G')
    digits[1] = input_item.count('O') - digits[2] - digits[0] - digits[4]
    
    if digits[1] < 0:
        digits[1] = 0
        
    digits[3] = input_item.count('T') - digits[2] - digits[8]
    
    if digits[3] < 0:
        digits[3] = 0       
    
    digits[7] = input_item.count('S') - digits[6]
    
    if digits[7] < 0:
        digits[7] = 0 
        
    digits[5] = input_item.count('F') - digits[4]

    if digits[5] < 0:
        digits[5] = 0  
        
    digits[9] = input_item.count('I') - digits[6] - digits[8] - digits[5]
    
    if digits[9] < 0:
        digits[9] = 0      
        
          
          
    number = []
    
    for i in range(len(digits)):
        for j in range(digits[i]):
            number.append(i)           
    
    number.sort()
            
    return number
    

   
    
    
    
input_lines = read_lines('input.txt')
input_lines = clean_up(input_lines)    



T_str = input_lines[0]
T = int(T_str)

solutions = []


for i in range(1, len(input_lines)):
    current_test = input_lines[i]
    current_solution = solve_problem(current_test)
    current_solution = ''.join(str(e) for e in current_solution)
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
    










