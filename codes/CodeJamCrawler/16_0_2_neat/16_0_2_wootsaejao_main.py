from multiprocessing import Pool
import sys
import os

def debug(*args):
    if os.environ.get('DEBUG'):
        print(*args)

def textToList(text):
    result = []
    for c in text:
        if c == '-':
            result.append(0)
        elif c == '+':
            result.append(1)
    return result

assert textToList('--+-+') == [0, 0, 1, 0, 1]

def allPancakesAreHappy(pancakes):
    return all(pancakes)

assert allPancakesAreHappy([1,1,1,1,1]) == True
assert allPancakesAreHappy([1,0,0,1,1]) == False

def manuever(pancakes, idx):
    cut = pancakes[:idx+1]
    return list(reversed(cut)) + pancakes[idx+1:]

assert manuever([1,2,3,4,5], 2) == [3,2,1,4,5]
assert manuever([1,0], 1) == [0,1]
assert manuever([1, 0, 1, 1, 1, 1, 1, 1, 1, 0], 1) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]

def flip(pancakes):
    result = []
    for idx, c in enumerate(pancakes):
        if c == 0:
            result.append(1)
        else:
            result += pancakes[idx:]
            break
    return result

assert flip([0,0,0,1,1,0,1]) == [1,1,1,1,1,0,1]
assert flip([0,1]) == [1,1]


INPUT_LINES = 1  # number of input lines per case

def solver(args):

    debug()
    debug()
    pancakes = textToList(args[0])
    # debug('start:', pancakes)

    count = 0
    tmp = []
    while True:
    # for _ in range(100):
        topNeedFlip = False
        doManueverNow = False
        doFlipNow = False
        allAreHappy = False
        foundUnhappy = False

        # case no happy pancakes found
        happyPancakes = list(filter(lambda x: x == 1, pancakes))
        if not happyPancakes:
            count += 1
            break

        # all are happy
        if len(happyPancakes) == len(pancakes):
            break

        debug('pancakes:', pancakes)
        if pancakes[0] == 0:
            debug('topNeedFlip')
            topNeedFlip = True

        for idx, cake in enumerate(pancakes):
            debug('-- idx:', idx)

            if (not topNeedFlip
                    and cake != 1
                    and len(pancakes) == idx + 1): # this is the last, and not happy
                debug('-- last')
                doManueverNow = True
                position = idx
            elif cake == 0:
                debug('foundUnhappy')
                foundUnhappy = True
                continue
            elif cake == 1:
                debug('-- 1')
                if topNeedFlip:
                    debug('doFlipNow')
                    doFlipNow = True
                    position = idx-1

                elif foundUnhappy:
                    debug('doManueverNow')
                    doManueverNow = True
                    position = idx-1

            if doManueverNow:
                debug('doManueverNow', pancakes, position)
                tmp = manuever(pancakes, position)
                debug(tmp)
                count += 1
                break

            if doFlipNow:
                debug('doFlipNow')
                tmp = flip(pancakes)
                count += 1
                if allPancakesAreHappy(tmp):
                    debug('all happy:', tmp)
                    allAreHappy = True
                break

        # check pancakes state, break if all pancakes are happy
        if allAreHappy:
            break
        else:
            debug('updatePancakes')
            pancakes = tmp

    return count

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
