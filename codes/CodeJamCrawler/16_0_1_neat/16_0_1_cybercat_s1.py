import sys

"""
num_input  = int(raw_input())
input_lst = []
for i in range(1, num_input+1):
    input_lst.append(int(raw_input()))
"""
input_lst = []
fd = open(sys.argv[1], 'r')
c=1
while True:
    line = fd.readline()
    if line =="":
        break
    
    if c ==1:
        num_input = int(line)
        
    else:
        input_lst.append(int(line))

    c = c+1
    

cnt =1


for in_val in input_lst:
    
    digit =[]

    for i in range(1, 201):
        
        result = str(in_val *i)

        for j in range(0, len(result)):
            if result[j] in digit:
                pass
            else:
                digit.append(result[j])


        if len(digit)== 10:
            break

    if len(digit) <10:
        print "Case #%d: "%cnt+"INSOMNIA"
    else:
        print "Case #%d: "%cnt + result

    cnt = cnt+1

