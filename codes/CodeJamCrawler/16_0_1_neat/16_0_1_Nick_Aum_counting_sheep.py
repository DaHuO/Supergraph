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
    
    

def solve_counting_sheep(current_num):
    last_seen_number = 'INSOMNIA'
    
    if current_num != 0:
        digits_remaining = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        multiplyer = 1
        
        while True:
            num_mult = current_num * multiplyer
            num_mult_str = str(num_mult)
            nums_seen = set()
            
            for digit in digits_remaining:
                if digit in num_mult_str:
                    nums_seen.add(digit)
                    
            if nums_seen:
                for digit in nums_seen:
                    digits_remaining.remove(digit)
                    
            if len(digits_remaining) == 0:
                last_seen_number = num_mult_str
                break
            
            multiplyer += 1
#            print digits_remaining
#            if multiplyer == 9:
#                break
            
    return last_seen_number
    

   
    
    
    
input_lines = read_lines('input.txt')
input_lines = clean_up(input_lines)    



T_str = input_lines[0]
T = int(T_str)

solutions = []


for i in range(1, len(input_lines)):
    current_test = input_lines[i]
    current_solution = solve_counting_sheep(int(current_test))
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
    










