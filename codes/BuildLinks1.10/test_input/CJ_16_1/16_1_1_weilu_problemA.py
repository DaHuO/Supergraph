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

for i in range(1,T+1):
    word = lines[i].rstrip('\n')
    head = word[0]
    winner = ''
    for letter in word:
        if(head<=letter):
            head = letter
            winner = letter + winner
        else:
            winner += letter
    # print(winner)
    print("Case #"+str(i)+": "+winner )#print('happy')
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
