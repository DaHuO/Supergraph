__author__ = 'hannahkim'

import sys
import numpy as np

input_file = sys.argv[1]
output_file = 'out_'+input_file
input = open(input_file,'r')
output = open(output_file, 'w')
n = int(input.readline())
for i in range(1,n+1):
    str_p = input.readline().rstrip('\n')
    prev = str_p[-1]
    if prev == '+':
        num = 0
    else:
        num = 1
    for j in range(len(str_p)-2,-1,-1):
        current = str_p[j]
        if prev != current:
            num += 1
        prev = current
    print 'CASE #'+str(i)+': '+str(num)
    output.write('CASE #'+str(i)+': '+str(num)+'\n')
input.close()
output.close()