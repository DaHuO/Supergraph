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
    input = open('B-large.in', 'r')
    numCases = int(input.readline().strip())

    case = 0

    for line in input:
        case = case + 1
        calcPancakes(line.strip(), case)

def calcPancakes(cakes, case):
    flips = 0

    while not isDone(cakes):
        if cakes[0] == "+":
            firstBlank = cakes.find("-")
            cakes = flip(cakes[0:firstBlank]) + cakes[firstBlank:]

        else: #cakes[0] == '-':
            #flip all from the top to the start of the bottom contiguous pluses
            lastBlank = cakes.rfind("-")
            cakes = flip(cakes[0:lastBlank+1]) + cakes[lastBlank+1:]

        flips = flips + 1
        continue

    print "Case #{0}: {1}".format(case, flips)
    return

def flip(cakes):
    return "".join(map(lambda x: "+" if (x == "-") else "-", cakes[::-1]))

def isDone(cakes):
    return all([x == "+" for x in cakes])

if __name__ == '__main__':
    main()
