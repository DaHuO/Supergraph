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



def find_largest_num(test):
    if test == 0:
        return -1

    found = [0 for i in range(10)]

    testcounter = test
    while sum(found) != 10:
        for i in str(testcounter):
           found[int(i)] = 1
        testcounter = testcounter + test

    return testcounter -  test



numTests = int(f.readline())
# numTests = 200
for i in range(numTests):
    test= int(f.readline())
    # test= i
    ret = find_largest_num(test)
    if ret == -1:
        wr.write("Case #%d: %s\n"%(i+1,"INSOMNIA"))
    else:
        wr.write("Case #%d: %d\n"%(i+1,ret))
