from common import *

def main(casenum):
    x = readline()
    x += '+'

    count = 0
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:
            count += 1
    writecase(casenum, count)

run(main)
