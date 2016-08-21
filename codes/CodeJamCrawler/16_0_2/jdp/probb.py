import argparse
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("of")
args = parser.parse_args()

print args.of

f=open(args.inputfile,"r")
wr=open(args.of,"w")


def flip(test,n):
    output = test[0:n]
    output.reverse()
    output=list(map(lambda x:int(not x), output))
    return output + test[n:]

def flip_right_most(test):
    if test[0] == 1:
        test[0] = 0
        counter = 1
        while test[counter] == 1:
            test[counter] = 0
            counter +=1
        return test
    for i,val in reversed(list(enumerate(test))):
        if val == 0:
            return flip(test,i+1)
    return test

def find_min_flips(test):
    count = 1
    while sum(test) != len(test):
        test = flip_right_most(test)
        count += 1
    return count - 1

numTests = int(f.readline())
# numTests = 200
for i in range(numTests):
    stack = []
    test = f.readline()
    for symbol in test:
        if symbol=='-':
            stack.append(0)
        elif symbol == '+':
            stack.append(1)
    ret = find_min_flips(stack)
    wr.write("Case #%d: %d\n"%(i+1,ret))
