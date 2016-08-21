import sys
import os

def main(in_file):
    inf = open(in_file)
    outf = open(in_file + ".result", "w")

    numlines = int(inf.readline())

    for casenum in range(1, numlines+1):
        (origlen, iteration, tries) = map(lambda x: int(x), inf.readline().split(" "))

        # trivial case for tries == origlen
        res = " ".join(map(lambda x: str(x), range(1, origlen+1)))

        result(casenum, res, outf)

    outf.close()
    inf.close()

def result(casenum, result, outf):
    s = "Case #%d: %s\n" % (casenum, result)
    print s,
    outf.write(s)

if __name__ == "__main__":
    main(sys.argv[1])