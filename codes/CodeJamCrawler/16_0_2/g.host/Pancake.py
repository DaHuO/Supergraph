def parseIn(inputFile):
    cases = 0
    case_N =[]
    with open(inputFile,"r") as f_in:    
        cases = int(f_in.readline())
        for line in f_in.readlines():
            case_N.append(line[0:len(line)-1])
    f_in.closed
    return cases, case_N

def parseOut(finList):
    with open("B-large.out",'w') as f_out:
        for i in range(len(finList)):
            x = 'Case #{}: {}\n'.format(i+1,finList[i])
            f_out.write(x)
    f_out.closed

def main():
    def flip(stck, numEl):
        retStck = ''
        toFlip = stck[0:numEl]
        toKeep = stck[numEl:]
        for item in reversed(toFlip):
            if item == '-':
                retStck += '+'
            else:
                retStck += '-'
        for item in toKeep:
            retStck += item
        return retStck
    def genFin(numEl):
        finStk = ''
        for i in range(numEl):
            finStk += '+'
        return finStk
    cases, case_N = parseIn("B-large.in")
    finVal = []
    for case in range(cases):
        stack =  case_N[case]
        numEl = len(stack)
        finStack = genFin(numEl)
        numFlips = 0
        i = 0
        while stack != finStack:
            i += 1
            if(stack[-i] == '-'):
                flippedstack = flip(stack, numEl-i+1)[:]
                numFlips += 1
                if flippedstack[-i] == '-':
                    toFlip = 0
                    for item in stack:
                        if item == '+':
                            toFlip += 1
                        else:
                            break
                    flippedstack = flip(stack,toFlip)[:]
                    flippedstack = flip(flippedstack, numEl-i+1)
                    numFlips += 1
                stack = flippedstack
        finVal.append(numFlips)
    parseOut(finVal)

main()