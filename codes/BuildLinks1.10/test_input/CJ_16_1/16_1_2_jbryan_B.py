from math import *
from itertools import accumulate

#input_file = open('B-sample.in','r')
#input_file = open('B-small-attempt1.in.txt','r')
input_file = open('B-large.in.txt','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('B.txt','w')

debug=0

###################

case_start=1
while case_num<=num_cases:
    N=int(lines[case_start])
    L=[]
    for i in range(2*N-1):
        L+=list(map(int,lines[case_start+1+i].split(' ')))

    ans = []
    for i in range(2501):
        c=L.count(i)
        if c%2==1:
            ans.append(i)
    ans.sort()
    
    output_text += 'Case #'+str(case_num)+': ' + ' '.join(map(str,ans)) + '\n'

    if debug: print(L)
    if debug: print(ans)
            
    #ans = max(longest)
    #output_text += ans+'\n'
    case_num += 1
    case_start += 2*N


if debug: print('\n'+output_text)
output_file.write(output_text)
input_file.close()
output_file.close()
