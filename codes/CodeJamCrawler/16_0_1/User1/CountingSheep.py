__author__ = 'dabhishek'

import sys
from sets import Set
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


def countingSheep(n):
    s = Set()
    for i in range(1, 100):
        v=i*n
        for c in str(v):
            s.add(int(c))
        if s.__len__() == 10:
            return v
    return 'INSOMNIA'


def main(args):
    openFile(sys.argv[0])
    lines = readInput(sys.argv[1])
    if lines is not None:
        cases = int(lines[0])
        for case in range(1, cases+1):
            out = countingSheep(int(lines[case]))
            outputFormatted = 'Case #' + str(case) + ': ' + str(out)
            writeOutput(f,outputFormatted)
    closeFile(f)


if __name__ == '__main__':
    main(sys.argv)