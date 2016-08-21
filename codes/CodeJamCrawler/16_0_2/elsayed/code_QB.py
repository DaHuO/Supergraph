#read input file 
with open('input.txt') as input_file:
    lines = input_file.readlines()
    
txt = open("output.txt", "ab")

case = []
N_lines = 1
N_case = int(lines[0])

#case array
for i in range(1,N_case+1,N_lines):
    case.append(lines[i].strip())
    


for i in range(0,len(case)):
    stack = []
    counter = 0
    for ch in case[i]:
        stack.insert(0,ch)
    while len(stack) !=0:
        if stack[0] == '+':
            stack.pop(0)
        elif stack[0] == '-':
            for j in range(0,len(stack)):
                if stack[j] == '+':
                    stack[j] = '-'
                elif stack[j] == '-':
                    stack[j] = '+'
            counter += 1
            
    out ="Case #"+str(i+1)+": "+str(counter)+"\n"
    txt.write(out)
    
txt.close()          
        
