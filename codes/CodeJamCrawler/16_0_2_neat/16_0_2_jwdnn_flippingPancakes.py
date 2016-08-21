#Flipping pancakes

def flip(stack, i):
    newStack = ''
    portion = list(stack[:i+1])
    for i in range(len(portion)):
        if portion[i] == "+":
            portion[i] = '-'
        else:
            portion[i] = '+'
    newStack = newStack.join(portion) + stack[i+1:]
    return newStack

def findRun(stack):
    counter = 0
    sym = stack[counter]
    while sym == stack[counter]:
        counter += 1
        if counter == len(stack):
            break
    return counter-1
    
#open files
inputFile = open('B-small-attempt0.in','r')
out = open("pancakeOut.out",'w')

T = int(inputFile.readline().strip())

for t in range(T):
    stack = inputFile.readline().strip()
    flips = 0
    while stack.find('-') != -1:
        i = findRun(stack)
        stack = flip(stack,i)
        flips += 1
    out.write("Case #%d: "%(t+1)+str(flips)+'\n')

inputFile.close()
out.close()    