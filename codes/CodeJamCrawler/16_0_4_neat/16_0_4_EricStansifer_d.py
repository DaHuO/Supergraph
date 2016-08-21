from common import *

def main(casenum):
    k, c, s = readints()
    res = ''
    for i in range(s):
        res += ' ' + str(i + 1)
    writecase(casenum, res)

run(main)
