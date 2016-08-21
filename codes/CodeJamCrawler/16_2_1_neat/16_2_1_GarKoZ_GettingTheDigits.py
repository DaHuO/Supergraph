def getDigit(strnum):
    numdict = {}
    for ele in strnum:
        if ele in numdict:
            numdict[ele] += 1
        else:
            numdict[ele] = 1
    return numdict

numCharList = [{'Z':1,'E':1, 'R':1, 'O':1},
            {'E':1, 'N':1, 'O':1},
            {'T':1,'W':1,'O':1},
            {'T':1,'E':2, 'R':1, 'H':1},
            {'F':1,'U':1, 'R':1, 'O':1},
            {'F':1,'E':1, 'I':1, 'V':1},
            {'S':1,'I':1, 'X':1 },
            {'S':1,'E':2, 'V':1, 'N':1},
            {'I':1,'E':1, 'G':1, 'H':1, 'T':1},
            {'N':2,'E':1, 'I':1}]

def checkAllZero(numdict):
    for ele in numdict:
        if numdict[ele] != 0:
            return False
    return True

def containMinus(numdict):
    for ele in numdict:
        if numdict[ele] < 0:
            return True
    return False


answer = []
def recurse(numdict, result, startI):
    global answer
    if checkAllZero(numdict):
        #print "get answer"
        answer =  list(result)
        #print answer
    
    for i in range(startI, len(numCharList)):
        ele = numCharList[i]
        temp = dict(numdict)
        for elechar in ele:
            notContain = False
            if elechar in temp: 
                temp[elechar] -= ele[elechar]
            else:
                notContain = True
                break
        if notContain :
            continue
        if containMinus(temp):
            continue
        result.append(i)
        recurse(temp, result, i)
        result.remove(i)

def wrappedRec(numstr):
    global answer
    answer = []
    recurse(getDigit(numstr), [], 0)    
    #return sorted(answer)
    answer = sorted(answer)
    ansstr = ''
    for ele in answer:
        ansstr += str(ele)
    return ansstr

f = open("A-small-attempt0(3).in", "r")

T = int(f.readline())

for x in xrange(0, T):
    readline = f.readline().strip()
    print "Case #" + str(x+1) + ": " + wrappedRec(readline)
        