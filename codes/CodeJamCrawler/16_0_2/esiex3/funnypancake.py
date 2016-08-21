__author__ = 'gosu'

from math import log


def main():
    inp = open("input.in")
    out = open("pancakeout.txt", 'w')
    c = int(inp.readline())
    casenum = 1
    for x in range(c):
        case = inp.readline().strip()
        flips = 0
        for i in range(1, len(case)):
            if case[i] != case[i-1]:
                flips += 1
        if case[-1] == '-':
            flips += 1
        print("Case #{0}: {1}".format(casenum, flips))
        out.write("Case #{0}: {1}".format(casenum, flips))
        out.write('\n')
        casenum += 1
    out.close()


if __name__ == '__main__':
    main()