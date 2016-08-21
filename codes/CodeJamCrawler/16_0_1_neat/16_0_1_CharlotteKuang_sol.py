import sys

def countingSheep(num):
    if num == 0: return "INSOMNIA"

    numDict = {}
    numCount = 0
    
    cur = num
    while numCount < 10:
        tmp = cur 
        while tmp > 0:
            mod = tmp % 10
            if not mod in numDict:
                numCount += 1
                numDict[mod] = True
            tmp /= 10
        cur += num  
    return cur - num

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    
    content = (f.read()).split("\n")

    caseNum = int(content[0])

    for i in range(caseNum):
        case = int(content[i+1])
        print "Case #%i: %s" % (i+1, countingSheep(case))
