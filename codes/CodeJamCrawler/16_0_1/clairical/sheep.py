import sys, os
import fileinput
import math



def getSheep(file):
    n = int(file.readline())
    allSeen = int(math.pow(2, 10)-1)
    for i in range(n):
        baseNum = int(file.readline())
        insomnia = False
        multiple = 1
        seen = 0
        if (baseNum == 0):
            insomnia = True

        while not insomnia:
            curVal = multiple*baseNum
            while curVal:
                digit = curVal % 10
                seen = seen | (1 << digit)
                curVal //=10
            if (seen & allSeen) == allSeen:
                curStr = "Case #" + str(i+1) + ": " + str(multiple*baseNum)
                print curStr
                break;
            multiple += 1
            if multiple > 200:
                insomnia = True
        if insomnia:
            print "Case #" + str(i + 1) +  ": INSOMNIA"



if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    getSheep(f)
    f.close()