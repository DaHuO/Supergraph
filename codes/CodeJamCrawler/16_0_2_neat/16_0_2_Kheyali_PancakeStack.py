
def flipStack(stack):
    newString = []
    for i in range(len(stack)):
        if(stack[i] == '+'):
            newString.append('-')
        else:
            newString.append('+')
    return ''.join(newString)

def isAllHappy(string):
    for i in range(len(string)):
        if(string[i] != '+'):
            return False
    return True
def recursivelyFlipStack(stack):
    count = 0
    while(isAllHappy(stack) == False):
        for i in range(len(stack)-1,-1,-1):            
            if(stack[i] !='+'):
                newString = flipStack(stack[:i+1])
                count += 1
                stack = newString
    return count
def output(flipcount):
    count = 1
    for item in flipcount:
        print("Case #"+str(count)+": " + str(item))
        count += 1
def processStack(panCakeStack):
    flipcount = []
    for pile in panCakeStack:
        count = recursivelyFlipStack(pile)
        flipcount.append(count)
    output(flipcount)

#MAin
T = int(input().strip())
panCakeStack =[]
for i in range (T):
    panCakeStack.append(input().strip())

processStack(panCakeStack)
