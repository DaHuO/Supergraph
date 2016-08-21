#!/usr/bin/env python


import sys


__outputTemplate = 'Case #{0}: {1}\n'
__forever = 'INSOMNIA'
__max = 1000


def getLastNumber(n):
    if n == 0:
        return __forever
    seen = [False] * 10
    i = 0
    while i < __max and not all(seen):
        i += 1
        current = n * i
        for x in str(current):
            j = int(x)
            seen[j] = True
    return current


def action(inFile, outFile):
    case = 0
    t = int(inFile.readline())
    for line in inFile.readlines():
        case += 1
        assert case <= t
        n = int(line)
        result = getLastNumber(n)
        outFile.write(__outputTemplate.format(case, result))


def main():
    """
    command line arguments are:
        input path
        output path (will overwrite existing)
    """
    assert len(sys.argv) == 3
    inputPath, outputPath = sys.argv[1:3]
    with open(inputPath, 'r') as inFile:
        with open(outputPath, 'w+') as outFile:
            action(inFile, outFile)


if __name__ == '__main__':
    main()
