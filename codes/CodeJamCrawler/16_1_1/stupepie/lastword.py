__author__ = 'hannahkim'

import sys

input_file = sys.argv[1]
output_file = 'out_'+input_file
input = open(input_file,'r')
output = open(output_file, 'w')
n = int(input.readline())
print n
for i in range(1,n+1):
    str_m = input.readline().rstrip('\n')
    str_fin = str_m[0]
    for j in range(1,len(str_m)):
        if str_fin[0] <= str_m[j]:
            str_fin = str_m[j] + str_fin
        else:
            str_fin = str_fin + str_m[j]
        # print str_fin
    output.write('CASE #'+str(i)+': '+str_fin+'\n')
    print 'CASE #'+str(i)+': '+str_fin
input.close()
output.close()