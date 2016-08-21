__author__ = 'Vinayak'
import sys

def get_digits(N):
    N_string=str(N)
    return [int(ch) for ch in N_string]

data=list()
output_data=''

with open("A-large.in",'r') as f:
    for line in f.readlines():
        data.append(line)

test_case=int(data.pop(0))
i=0
while i<test_case:
    num_stack=set()
    N_stack=[]
    N=int(data.pop(0))
    num_stack.update(get_digits(N))
    j=1
    insomnia=False
    while len(num_stack) != 10:
        j=j+1
        if N*j in N_stack:
            insomnia=True
            output_data+="Case #"+str(i+1)+": "+str("INSOMNIA")+"\n"
            break
        N_stack.append(N*j)
        num_stack.update(get_digits(N*j))
    #print(num_stack)
    if insomnia==False:
        output_data+="Case #"+str(i+1)+": "+str(N*j)+"\n"
    i=i+1

#print(output_data)
with open("outputfile.in",'w') as f:
    f.write(output_data)