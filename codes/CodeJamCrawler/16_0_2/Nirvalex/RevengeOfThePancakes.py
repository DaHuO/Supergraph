#Input
#-
#-+
#+-
#+++
#--+- > +++- > ---- > ---- > ++++

#Output
#Case #1: 1
#Case #2: 1
#Case #3: 2
#Case #4: 0
#Case #5: 3

def pancakes(case,stack):
    stack=[x for x in stack]
    flips=0

    while True:
        isUniform = uniform(stack)
        if isUniform == '+':
            return "Case #"+str(case)+": "+str(flips)+"\n"
            return
        elif isUniform == '-':
            return "Case #"+str(case)+": "+str(flips+1)+"\n"
            return
        fIndex = flipIndex(stack)
        stack = flipStack(stack,fIndex)
        flips+=1

def stackAsString(stack):
    stackString = ''
    for x in stack:
        stackString+=x
    return stackString

def flipIndex(stack):
    firstPancake=stack[0]
    stackDepth=len(stack)
    i=stackDepth-1
    lastPancake=stack[i]

    if lastPancake=='+':
        while stack[i]=='+' and i>0:
            i-=1

    if i==-1:
        return -1
    else:
        lastPancake=stack[i]

    if firstPancake==lastPancake:
        if firstPancake=='-':
            return i
        else:
            return "ERROR"
    else:
        if firstPancake=='+':
            j=0
            while stack[j]=='+':
                j+=1
            return j-1
        else:
            return "ERROR"


def uniform(stack):
    numMinus=0
    for p in stack:
        if p=='-':
            numMinus+=1
    if numMinus==len(stack):
        return '-'
    elif numMinus==0:
        return '+'
    else:
        return 'n'

def flipStack(stack,flipBeforeIndex):
    flippedStack=[]
    i=flipBeforeIndex
    while i >= 0:
        if stack[i]=='-':
            flippedStack.append('+')
        else:
            flippedStack.append('-')
        i-=1
    return flippedStack+stack[flipBeforeIndex+1:]

def readTestFile(fileName):
    r = open('pancakes2.out', 'w')
    with open(fileName) as f:
        i=0
        for line in f:
            if i==0:
                NumberOfRecords=int(line)
            else:
                r.write(pancakes(i,line.strip('\n')))
            i+=1  


readTestFile('pancakes.in')


