#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rayan
#
# Created:     20/04/2016
# Copyright:   (c) Rayan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calc(n):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    checks = [False, False, False, False, False, False, False, False, False, False]
    counter = 1
    looking = True
    while (looking):
        currentString = str(counter * n)
        stringList = []
        for i in currentString:
            stringList.append(i)
        for each in stringList:
            intEach = int(each)
            if (checks[intEach - 1] == False):
                checks[intEach -1] = True;
        metaCount = 0
        for each in checks:
            if each == True:
                metaCount += 1
        if metaCount == 10:
            looking == False
            return counter * n
        counter += 1




def main():
    N = []
    f = open('A-large.in', 'r')
    T = int(f.readline())
    linelist = f.readlines()
    start = 1
    for all in linelist:
        N.append(int(all))
    answers = []
    for each in N:
        if each == 0:
            numA = "INSOMNIA"
        else:
            numA = calc(each)
        answers.append(numA)
    for each in range(len(answers)):
        caseNo = str(each + 1)
        print("Case #" + caseNo + ": " + str(answers[each]))


if __name__ == '__main__':
    main()
