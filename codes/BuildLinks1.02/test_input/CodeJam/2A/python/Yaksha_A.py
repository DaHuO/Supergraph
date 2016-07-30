import logging
from logging import debug as d
from itertools import combinations, permutations
import copy

EPS = 10 ** -6

logging.basicConfig(level=logging.DEBUG, format=('%(funcName)s(%(lineno)d):  %(message)s'))

def p(**kwargs):
    printstr = ''
    for (key, var) in kwargs.items():
        printstr += ("%s=%s\t" % (key, var))

    return printstr


def doSolve(filename, solver, log=False):
    with open(filename) as infile:
        with open(filename + ".out", 'w') as outfile:
            numCases = int(infile.readline())

            for i in range(numCases):
                inputs = parseTestCase(infile)
                result = solver(inputs)
                if log:
                    print(inputs)
                    print(result)
                    print(" ")

                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    return [int(x) for x in file.readline().strip().split()]

def solver(values):
    r = values[1]
    p = values[2]
    s = values[3]

    bestresult = None

    players = ['r'] * r + ['p'] * p + ['s'] * s
    for p in permutations(players):
        if willfinish(p):
            result = ''.join(p)
            if bestresult is None:
                bestresult = result
            else:
                bestresult = result if result < bestresult else bestresult

    if bestresult is None:
        return "IMPOSSIBLE"
    else:
        return bestresult.upper()

def willfinish(players):

    nextround = players
    while len(nextround) > 1:
        thisround = copy.copy(nextround)
        nextround = []

        while thisround:
            win = winner(thisround[0], thisround[1])
            if win is None:
                return False

            nextround.append(win)
            thisround = thisround[2:]

    return True

def winner(a, b):
    if a == 'r' and b == 's':
        return a

    if a == 'r' and b == 'p':
        return b

    if a == 's' and b == 'r':
        return b

    if a == 's' and b == 'p':
        return a

    if a == 'p' and b == 'r':
        return a

    if a == 'p' and b == 's':
        return b

    return None


#FILENAME = r"test.in"
FILENAME = r"K:\downloads\A-small-attempt0.in"
doSolve(FILENAME, solver, True)
