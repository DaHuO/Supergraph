f = open('B-large.in')
# f = open('test.in')

import sys
sys.stdout = open('out', 'w')

T = f.readline()
for case in range(int(T)):
    l = list(f.readline().replace('\n', ''))
    count = 0
    while not all('+' == char for char in l):
        idx = 0
        for i in range(len(l)):
            if l[i] == '-':
                idx = i
        for i in range(idx+1):
            if l[i] == '+':
                l[i] = '-'
            else:
                l[i] = '+'
        count += 1
            
    print "Case #"+str(case+1)+":", count
    
