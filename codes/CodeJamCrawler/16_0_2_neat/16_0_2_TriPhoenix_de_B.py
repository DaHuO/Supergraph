import sys
import os

def main(in_file):
    inf = open(in_file)
    outf = open(in_file + ".result", "w")

    numlines = int(inf.readline())

    for casenum in range(1, numlines+1):
        pancakesr = reversed(inf.readline()[:-1])
        pancakes = map(lambda x: x == '+', pancakesr)

        flips = 0
        for x in range(len(pancakes)):
            doflip = not pancakes[x]
            if doflip:
                for y in range(x, len(pancakes)):
                    pancakes[y] = not pancakes[y]
                flips += 1
        res = str(flips)
        result(casenum, res, outf)

    outf.close()
    inf.close()

def result(casenum, result, outf):
    s = "Case #%d: %s\n" % (casenum, result)
    print s,
    outf.write(s)

if __name__ == "__main__":
    main(sys.argv[1])