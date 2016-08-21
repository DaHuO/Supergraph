#!/usr/bin/env python


import sys


__outputTemplate = 'Case #{0}: {1}\n'


def flip(pancakes):
    return [not p for p in reversed(pancakes)]


def flipAfter(stack, i):
    return flip(stack[:i+1]) + stack[i+1:]


def flipPoint(stack):
    for i in range(len(stack) - 1):
        if stack[i] != stack[i+1]:
            return i
    return len(stack) - 1


def minimumFlips(stack, verbose=False):
    maxFlips = len(stack)
    flips = 0
    while flips < maxFlips and not all(stack):
        flips += 1
        if verbose:
            print('start stack: {}'.format(stack))
        i = flipPoint(stack)
        if verbose:
            print('flip at: {}'.format(i))
        if i >= 0:
            stack = flipAfter(stack, i)
        if verbose:
            print('end stack: {}'.format(stack))
    return flips


def stringToStack(s):
    return [p == '+' for p in s.strip()]


def action(inFile, outFile):
    case = 0
    t = int(inFile.readline())
    for line in inFile.readlines():
        case += 1
        assert case <= t
        x = stringToStack(line)
        result = minimumFlips(x)
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
