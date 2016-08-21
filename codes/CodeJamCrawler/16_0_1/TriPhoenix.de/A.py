import sys
import os

def main(in_file):
    inf = open(in_file)
    outf = open(in_file + ".result", "w")

    numlines = int(inf.readline())

    for casenum in range(1, numlines+1):
        number = int(inf.readline())

        if number == 0:
            res = "INSOMNIA"
        else:
            res = 0
            digits = set()
            curnum = number
            while len(digits) != 10:
                digits = digits.union(str(curnum))
                res = curnum
                curnum += number

        result(casenum, res, outf)

    outf.close()
    inf.close()

def result(casenum, result, outf):
    s = "Case #%d: %s\n" % (casenum, result)
    print s,
    outf.write(s)

if __name__ == "__main__":
    main(sys.argv[1])