#!/usr/bin/env python
# encoding: utf-8

def parseCase(line):
    return int(line.strip())


def solve(caseLine):
    n = parseCase(caseLine)
    if n == 0:
        return "INSOMNIA"
    digits = 0x0
    for i in range(1, 1000000):
        kn = i * n
        cn = kn
        while cn > 0:
            digits = digits | (1 << int(cn % 10))
            cn = int(cn / 10)
        if digits == 0x3FF:
            return str(kn)

    return "INSOMNIA"


def run(inputFile, outputFile):
    fp = open(inputFile, 'r')
    fw = open(outputFile, 'w')
    caseIndex = 0
    count = -1
    for line in fp:
        if (caseIndex == 0):
            count = int(line)
            caseIndex += 1
        else:
            fw.write("Case #%d: %s\n" % (caseIndex, solve(line)))
            caseIndex += 1
            count -= 1
        if (count == 0):
            break
    fp.close()
    fw.close()


if __name__ == "__main__":
    run("in", "out")