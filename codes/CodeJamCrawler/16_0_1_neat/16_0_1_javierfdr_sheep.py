# Google Code Jam 2016
# javierfdr@gmail.com
# Counting Sheep

import sys

# Naive implementation for the problem. Since the last name she will see is being asked, is getting
# simpler to actually compute the multiplications

def getLastCountedNumber(initNumber):
    counted = set()
    count = 1
    if (initNumber == 0):
        return 'INSOMNIA'

    next = initNumber
    for i in str(initNumber):
        counted.add(i)
    count = count+1

    while(len(counted) < 10):
        next = initNumber * count
        for i in str(next):
            counted.add(i)
        count = count+1

    return next

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):
 case = 'Case #'+str(c)+': '
 initNumber = int(in_file.readline())
 result= case+ str(getLastCountedNumber(initNumber))+'\n'
 out_file.write(result)