from multiprocessing import Pool
import sys

def textToList(f, text): return list( map(f, text.split()) )

def extractDigitSet(num):
    result = set()
    for c in str(num):
        result.add(int(c))
    return result

assert extractDigitSet(1234) == set([1, 2, 3, 4])

EXPECTED = set(range(10))

INPUT_LINES = 1  # number of input lines per case

def solver(args):
    result = None
    N = int( args[0] )
    numSet = set()
    for i in range(1, 500000):
        candidate = i * N
        extracted = extractDigitSet(candidate)
        numSet |= extractDigitSet(candidate)
        if not bool( numSet.symmetric_difference(EXPECTED) ):
            result = candidate
            break

    if not result:
        return 'INSOMNIA'

    return result

if __name__ == '__main__':
    totalCases = int( input() )

    # extract arguments
    caseArgsList = []
    for _ in range(totalCases):
        args = []
        for _ in range(INPUT_LINES):
            args.append(input())
        caseArgsList.append(args)

    # solve
    with Pool() as p:
        # results = map(solver, caseArgsList)
        results = p.map(solver, caseArgsList)  # use multi-cores
        for caseNumber, result in enumerate(results, 1):
            print('Case #{}: {}'.format(caseNumber, result))
