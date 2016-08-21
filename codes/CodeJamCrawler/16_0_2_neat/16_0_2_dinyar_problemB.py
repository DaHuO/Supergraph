#!/bin/python
filename = "B-large.in"

caseNum = 0
with open(filename) as f:
    numberOfProblems = int(f.readline().rstrip('\n'))
    for line in f:
        caseNum += 1
	l = line.rstrip('\n')
        flips = 0
        #if '-' not in l:
        #    print "Case #" + str(caseNum) + ":", flips
        #    continue
        stack = l
        #print "##############"
        #print "stack:", stack
        solved = False
        firstPancake = stack[0]
        #print 'firstPancake', firstPancake
        for i in range(0, len(stack)+1):
            blank = stack.find('-')
            if blank == -1:
                print "Case #" + str(caseNum) + ":", flips
                solved = True
                break

            if firstPancake == '+':
                flipPosition = stack.find('-')
                firstPancake = '-'
            else:
                flipPosition = stack.find('+')
                firstPancake = '+'
            #print 'flipPosition', flipPosition
            if flipPosition == -1:
                flipPosition = len(stack)
            subStack = stack[0:flipPosition]
            #print "substack:", subStack
            reversedSubStack = []
            for j in reversed(subStack):
                if j == '+':
                    reversedSubStack.append('-')
                elif j == '-':
                    reversedSubStack.append('+')
                else:
                    print "ERROR: This is not supposed to happen."
            #print "reversed substack:", reversedSubStack
            stack = ''.join(reversedSubStack) + stack[flipPosition:]
            #print "new stack:", stack
            flips += 1
        if solved == False:
            print "ERROR: Didn's solve Case #" + str(caseNum)

