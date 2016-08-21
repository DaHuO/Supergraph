#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input",
                    help="input file name")
parser.add_argument("-v", "--verbose", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()

f = open(sys.argv[1])
lines = f.readlines()
T = int(lines[0].rstrip('\n'))
N = int(lines[1].rstrip('\n'))
pos = 2
myn = 2500


for i in range(1,T+1):
    count = [0]*(myn+1)
    all_lines = []
    result = []
    for ii in range(2*N-1):
        one_line = [int(i) for i in lines[pos].rstrip('\n').split()]
        pos += 1
        for num in one_line:
            count[num] += 1
    # print(count)
    if i<T:
        N = int(lines[pos].rstrip('\n'))
        pos +=1


    # print(N)
    print("Case #"+str(i)+": ",end='')
    for num in range(1,myn+1):
        if(count[num]%2 != 0):
            print(num,end=' ')
    print()
    # # find the first row
    # smallest = 2500
    # first_line = []
    # for line in all_lines:
    #     if(line[0] < smallest):
    #         first_line = line
    #         smallest = line[0]
    # print(first_line)

    # use the first row to find the rest

    # print(winner)
    # print("Case #"+str(i)+": "+winner )#print('happy')
    # print(words)
    # digits = list(map(int,str(num)))
    # myset = set()
    # done =False
    # for j in range(1,101):
    #     temp = num*j
    #     myset |= set(list(map(int,str(temp))))
    #     if(len(myset) == 10):
    #         done = True
    #         print("Case #"+str(i)+": "+str(temp) )#print('happy')
    #         break
    # if(done == False):
    #     print("Case #"+str(i)+": INSOMNIA")
