import sys, itertools

input_file_name = 'B-large.in'
output_file_name = 'output2large.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()
num_cases = int(contents.pop(0))

def leftmost(l):
    ch = l[0]
    counter = 1
    for i in range(len(l)-1):
        if ch == l[i+1]:
            counter = counter + 1
        else:
            break
    return counter

def traverse(s):
    s = s.replace("\n", "")
    l = list(s)
    i = 0
    while l != []:
        if '-' in l:
            i = i + 1
        for j in range(leftmost(l)):
            l.pop(0)
    return i

for case in range (num_cases):

    stack = contents.pop(0)
    answer = traverse(stack)
    print('Case #{}: {}'.format(case+1, answer))
    print('Case #{}: {}'.format(case+1, answer), file = f_out)
  
f_in.close()
f_out.close()
