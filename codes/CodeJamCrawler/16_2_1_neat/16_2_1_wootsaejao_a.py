from multiprocessing import Pool
import sys

INPUT_LINES = 1  # number of input lines per case

# NUM_STR = {
#     3: 'THREE',
#     2: 'TWO',
#     7: 'SEVEN',
#     6: 'SIX',
#     8: 'EIGHT',
#     0: 'ZERO',
#     4: 'FOUR',
#     5: 'FIVE',
#     9: 'NINE',
#     1: 'ONE',
# }

NUM_STR = [
    (4, 'FOUR'),
    (2, 'TWO'),
    (6, 'SIX'),
    (0, 'ZERO'),
    (8, 'EIGHT'),

    (1, 'ONE'),
    (3, 'THREE'),
    (5, 'FIVE'),

    (9, 'NINE'),
    (7, 'SEVEN'),
]

def solver(args):
    #print()
    inputStr = args[0]
    # inputStr = 'ONTFWURONEI'
    # inputStr = 'NZOETOESEERRHINXOE'
    # inputStr = 'OVVIEIFNTWONTFOEOEWE'
    #print('input:', inputStr)
    result = ''

    for _ in range(inputStr.count('U')):
        for c in 'FOUR':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(4)
    #print(inputStr)

    for _ in range(inputStr.count('W')):
        for c in 'TWO':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(2)
    #print(inputStr)

    for _ in range(inputStr.count('X')):
        for c in 'SIX':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(6)
    #print(inputStr)

    for _ in range(inputStr.count('Z')):
        for c in 'ZERO':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(0)
    #print(inputStr)

    for _ in range(inputStr.count('G')):
        for c in 'EIGHT':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(8)
    #print(inputStr)

    for _ in range(inputStr.count('O')):
        for c in 'ONE':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(1)
    #print(inputStr)

    for _ in range(inputStr.count('H')):
        for c in 'THREE':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(3)
    #print(inputStr)

    for _ in range(inputStr.count('F')):
        for c in 'FIVE':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(5)
    #print(inputStr)

    for _ in range(inputStr.count('I')):
        for c in 'NINE':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(9)
    #print(inputStr)

    for _ in range(inputStr.count('V')):
        for c in 'SEVEN':
            idx = inputStr.find(c)
            inputStr = inputStr[:idx] + inputStr[idx+1:]
        result = result + str(7)
    #print(inputStr)

    # count = 0
    # while inputStr:
    #
    #     # for num, spell in reversed( sorted( list( NUM_STR.items() ), key=lambda x: len(x[1]) ) ):
    #     for num, spell in NUM_STR:
    #         #print('inputStr:', inputStr)
    #         #print('spell:', spell)
    #         if not inputStr:
    #             break
    #
    #         tmpInputStr = str(inputStr)
    #         fail = False
    #         for c in spell:
    #             idx = tmpInputStr.find(c)
    #             #print('c:', c)
    #             #print('idx:', idx)
    #             if idx > -1:
    #                 tmpInputStr = tmpInputStr[:idx] + tmpInputStr[idx+1:]
    #             else:
    #                 #print('fail')
    #                 fail = True
    #                 break
    #
    #         if not fail:
    #             result = result + str(num)
    #             inputStr = str(tmpInputStr)
    #
    #     # count += 1
    #     # if count > 1:
    #     #     sys.exit()
    #


    #print('result:', result)
    return ''.join(list(sorted(result)))

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
        results = map(solver, caseArgsList)
        # results = p.map(solver, caseArgsList)  # use multi-cores
        for caseNumber, result in enumerate(results, 1):
            print('Case #{}: {}'.format(caseNumber, result))
