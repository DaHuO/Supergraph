__author__ = 'dabhishek'

import sys
# Global Variables
global f


def readInput(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        lines = None
    return lines


def writeOutput(file, data):
    file.write(data)
    file.write('\n')


def openFile(filename):
    global f
    try:
        fname = filename + '.out'
        f = open(fname, 'w')
        return f
    except Exception as e:
        f = None


def closeFile(f):
    try:
        f.close()
    except Exception as e:
        print e.message


def countFlip(line):
    v = 0
    if line.__contains__('-'):
        stack = list(line)
        while stack.__contains__('-'):
            v += 1
            if stack[0] == '-':
                if not stack.__contains__('+'):
                    break
                else:
                    j = stack.index('+')
                    ## make all - -> +
                    for i in range(0, j):
                        stack[i] = '+'
            else:
                j = stack.index('-')
                ## make all + -> -
                for i in range(0, j):
                    stack[i] = '-'
    return v


def main(args):
    openFile(sys.argv[0])
    lines = readInput(sys.argv[1])
    if lines is not None:
        cases = int(lines[0])
        for case in range(1, cases + 1):
            out = countFlip(lines[case])
            #print lines[case],out
            outputFormatted = 'Case #' + str(case) + ': ' + str(out)
            #print outputFormatted
            writeOutput(f, outputFormatted)
    closeFile(f)


if __name__ == '__main__':
    main(sys.argv)