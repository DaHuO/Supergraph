import math
import itertools


def getAllBase(strNum):
    allBaseNum = []
    for i in range(2,10 + 1):
        allBaseNum.append(int(strNum, i))
    return allBaseNum

def getKTrivial(Num):
    for i in range(2, int(math.ceil(math.sqrt(Num)) + 1)):
        if Num % i == 0:
            return i
    return 0
    
def getAllNumber(InputN):
    result = []
    for ele in itertools.product('01', repeat=InputN):
        if ele[0] == '1' and ele[-1] == '1':
            result.append(''.join(ele))
    return result
    
def checkNumberGotAllKTrivial(Number):
    result = []
    Klist = []
    for numInBase in getAllBase(Number):
        remain = getKTrivial(numInBase)
        if  remain == 0:
            return False, []
        else:
            Klist.append(remain)
        result.append(numInBase)
    return result, Klist

def GetTestcase(InputN, InputJ):
    
    countj = 0
    for toBeCheckJ in getAllNumber(InputN):
        result, Klist = checkNumberGotAllKTrivial(toBeCheckJ)
        if result:
            tobePrint = toBeCheckJ
            #for numbase in result:
            #    tobePrint += ' ' + str(numbase)
            #tobePrint += '\n'
            for k in Klist:
                tobePrint += ' ' + str(k)
            
            print tobePrint
            countj += 1
        if countj >= InputJ:
            break
    #print 'countJ = ' + str(countj)

f = open("C-small-attempt0.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().strip()
    N, J = readline.split(' ')
    print "Case #" + str(x+1) + ":"
    GetTestcase(int(N), int(J))
    


