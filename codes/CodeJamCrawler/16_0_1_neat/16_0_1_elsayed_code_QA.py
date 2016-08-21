#read input file 
with open('input.txt') as input_file:
    lines = input_file.readlines()
    
txt = open("output.txt", "ab")

case = []
N_lines = 1
N_case = int(lines[0])

#case array
for i in range(1,N_case+1):
    case.append(lines[i])

for i in range(0,N_case):
    j = 2
    num = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]    
    N = str(int(case[i]))
    org_N = N
    if int(N)!=0:
        while num != range(0,10):
            for digit in N:
                N = str(int(org_N)*j)
                num[int(digit)] = int(digit)
            j = j+1
            
        output =  "Case #"+str(i+1)+": "+ str(int(N)-int(org_N))+"\n"
        print output
        txt.write(output)

    else:
        output =  "Case #"+str(i+1)+": INSOMNIA\n"
        print output
        txt.write(output)
        
txt.close()          
        
    
    
#print num
#print range(0,10)
