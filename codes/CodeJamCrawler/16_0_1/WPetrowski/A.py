#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wesley.Petrowski
#
# Created:     08/04/2016
# Copyright:   (c) Wesley.Petrowski 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    input = open('A-large.in', 'r')
    numCases = int(input.readline().strip())

    case = 0

    for line in input:
        case = case + 1
        calcSheep(int(line), case)

def calcSheep(startNum, case):
    if startNum == 0:
        print "Case #%d: INSOMNIA" % case
        return

    seen = [False] * 10

    mult = 0

    while not all(seen):
        mult = mult + 1
        updateSeen(seen, startNum * mult)

    print "Case #{0}: {1}".format(case, (startNum * mult))

def updateSeen(seen, num):
    while num != 0:
        seen[num % 10] = True
        num = num // 10

if __name__ == '__main__':
    main()
