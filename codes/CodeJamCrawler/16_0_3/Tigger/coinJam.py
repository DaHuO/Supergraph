import sys
import numpy
import itertools
def figureOutValue(value, base):
    tmpValue = 0
    place = 0
    reverse = str(value)[::-1]
    for c in reverse:
        tmpValue += int(c)*(base**place)
        place += 1
    return tmpValue



def createNum(n):
    for i in xrange(2**n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        yield s

def primageCheck(value):
    for i in xrange(2, (int)(value**.2)):
        if value % i == 0:
            return i
    return 0

#Sucky brute force way - yeild statement recursion would be much cleaner
def goThroughList(bitMove, count):
    #lst = list(itertools.product([0,1], repeat=bitMove-2))
    #value_list = ["".join(str(lst) for lst in pair) for pair in lst]
    num = 0
    print "Case #1:"
    myGen = createNum(bitMove-2)

    for x in myGen:
        x = "1" + x + "1"
        x = int(x)
                        
        mod_array = []
        for base in xrange(2, 11):
            mods = primageCheck(figureOutValue(x, base))
            if mods != 0:
                mod_array.append(mods)
            else:
                mod_array = []
                break
        
        if mod_array != []:
            print str(x) + " "  + " ".join(str(z) for z in mod_array)
            num += 1
            if count == num:
                break
def main():
    test = 32
    count = 500
    goThroughList(test, count)

main()
