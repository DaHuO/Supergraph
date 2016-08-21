numCases=int(input())
cases=[]
for i in range(0, numCases):
    cases.append(input().strip('\r'))
def isDone(cakes):
    for i in range(0, len(cakes)):
        if cakes[i]=='-':
            return False
    return True

def flip(index, cakes):
    flippedCakes=''
    for i in range(index, -1, -1):
        if cakes[i]=="-":
            flippedCakes+="+"
        else:
            flippedCakes+="-"
    for i in range(index+1, len(cakes)):
        flippedCakes+=cakes[i]
    return flippedCakes

def numTopPos(cakes):
    n=0
    i=0
    while cakes[i]=='+':
        n+=1
        i+=1
    return n

def solve(cakes):
    #print("curr stack:", cakes)
    if cakes=='':
        numFlips=0
    elif cakes[len(cakes)-1]=="+":
        numFlips=solve(cakes[:-1])
    elif cakes[0]=='-' and cakes[len(cakes)-1]=='-':
        numFlips=1+solve(flip(len(cakes)-1, cakes))
    elif cakes[len(cakes)-1]=='-' and cakes[0]=='+':
        numFlips=1+solve(flip(numTopPos(cakes)-1, cakes))
    return numFlips
        
for i in range(0, numCases):
    string="Case #"+str(i+1)+": "+str(solve(cases[i]))
    print(string)
