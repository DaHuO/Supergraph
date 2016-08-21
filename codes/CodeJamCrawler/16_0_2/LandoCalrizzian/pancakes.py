#!/usr/bin/python

maxTestCases = int(raw_input().strip())
happy = '+'
sad = '-'

for caseNum in xrange(1, maxTestCases + 1):
    pancakeStack = list(raw_input().strip())
    answer = 0
    stackHeight = len(pancakeStack)

    if stackHeight == 1:
        answer = 1
        if pancakeStack[0] == happy:
            answer = 0
        print 'Case #{}: {}'.format(caseNum, answer)

        continue

    happyStack = False

    while not happyStack:
        stackSet = set(pancakeStack)

        # Check to make sure the stack is happy
        if len(stackSet) == 1:
            omniPancake = stackSet.pop()
            # Stack is one mood now check if we need to go sad -> happy
            if omniPancake == sad:
                answer += 1
            break

        # Goal: Work our way to the bottom and make the pancakes the same when we detect mood swing
        pIndex = 1
        while (pIndex < stackHeight) and pancakeStack[pIndex - 1] == pancakeStack[pIndex]:
            pIndex += 1

        answer += 1
        # pIndex should point to the first change pancake mood
        pancakeStack = (list(pancakeStack[pIndex]) * pIndex) + pancakeStack[pIndex:]

    print 'Case #{}: {}'.format(caseNum, answer)
