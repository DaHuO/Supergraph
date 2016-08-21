__author__ = 'hannahkim'

import sys
import numpy as np

input_file = sys.argv[1]
output_file = 'out_'+input_file
input = open(input_file,'r')
output = open(output_file, 'w')
n = int(input.readline())
# int(input.readline())
print n
for i in range(1,n+1):
    m = int(input.readline())
    hasdigit = np.zeros(10)
    j = 1
    if m == 0:
        str_m = 'INSOMNIA'
    else:
        while sum(hasdigit) < 10:
            str_m = str(int(j*m))
            for k in range(0,len(str_m)):
                if hasdigit[int(str_m[k])] == 0:
                    hasdigit[int(str_m[k])] = 1
            j += 1
    output.write('CASE #'+str(i)+': '+str_m+'\n')
    print 'CASE #'+str(i)+': '+str_m
input.close()
output.close()