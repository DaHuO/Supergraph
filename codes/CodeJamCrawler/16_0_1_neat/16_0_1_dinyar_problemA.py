#!/bin/python
filename = "A-large.in"

caseNum = 0
with open(filename) as f:
    numberOfProblems = int(f.readline().rstrip('\n'))
    for line in f:
        caseNum += 1
	l = line.rstrip('\n')
        if l == '0':
            print "Case #" + str(caseNum) + ": INSOMNIA"
            continue
        numDict = set() 
        iteration = 1
        while True:
            num = int(l)*iteration
            iteration += 1
            for i in str(num):
                #print "Adding: ", i
                numDict.add(int(i))
            complete = True
            for i in range(0, 10):
                if i not in numDict:
                    complete = False
                    break
            if complete == True:
                print "Case #" + str(caseNum) + ":", num
                break
