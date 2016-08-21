from random import choice
import math

def isNotPrime(num):
    divList = []
    if num % 2 == 0 and num > 2:
        return True, 2
    else:
        for i in xrange(3, int(math.sqrt(num)) + 1, 2):
            if num%i == 0:
                return True,i
        return False,None
            

def checkIfValidNum(num_string):
    ret1, div1 = isNotPrime(long(num_string))
    if ret1 is False:
        return False, div1
    ret2, div2 = isNotPrime(long(num_string,2))
    if ret2 is False:
        return False, div2
    ret3, div3 = isNotPrime(long(num_string,3))
    if ret3 is False:
        return False, div3
    ret4, div4 = isNotPrime(long(num_string,4))
    if ret4 is False:
        return False, div4
    ret5, div5 = isNotPrime(long(num_string,5))
    if ret5 is False:
        return False, div5
    ret6, div6 = isNotPrime(long(num_string,6))
    if ret6 is False:
        return False, div6
    ret7, div7 = isNotPrime(long(num_string,7))
    if ret7 is False:
        return False, div7
    ret8, div8 = isNotPrime(long(num_string,8))
    if ret8 is False:
        return False, div8
    ret9, div9 = isNotPrime(long(num_string,9))
    if ret9 is False:
        return False, div9
    
    return True,[num_string, str(div2),str(div3),str(div4),str(div5),str(div6),str(div7),str(div8),str(div9),str(div1)]


def coinjam(n,j):
    counter = long(j)
    outputList =[]
    validNumDict = {}
    while counter > 0:
        isValidNum = False
        while isValidNum is False:
            num_string = ''.join(choice(['0','1']) for i in range(int(n)-2))
            num_string = "1" + num_string + "1"
            isValidNum,divList = checkIfValidNum(num_string)
            if isValidNum is True:
                if validNumDict.has_key(isValidNum):
                    isValidNum = False
                else:
                    outputList.append(divList)
        counter = counter - 1
    return outputList


def main():
    n_testcases = long(raw_input())
    counter = 1
    inputList = []
    while n_testcases > 0:
        inputL = raw_input().split()
        inputList.append([inputL[0],inputL[1]])
        n_testcases -= 1
    for val1,val2 in inputList:
        outList = coinjam(val1,val2)
        print "Case #%s:"%counter
        for numlist in outList:
            print " ".join(numlist)
        counter += 1

if __name__=="__main__":
    main()