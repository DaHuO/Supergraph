f = open("OutputLarge.txt", "w")

def flip():
    global pancakeStack
    rightmost = pancakeStack.rfind('-')
    
    newPancakeStack = ''
    for c in pancakeStack[:rightmost+1]:
        if c is '-':
            newPancakeStack += '+'
        else:
            newPancakeStack += '-'
    newPancakeStack += pancakeStack[rightmost+1:]
    pancakeStack = newPancakeStack

i = 0
for pancakeStack in open("B-large.in", "r"):
    if i != 0:
        pancakeStack = pancakeStack[:-1]
        
        if('-' not in pancakeStack):
            ans = 0
        else:
            flips = 0
            
            while '-' in pancakeStack:
                flip()
                flips += 1
            
            ans = flips
        ans = "Case #" + str(i) + ": " + str(ans) + "\n"
        f.write(ans)
    i += 1
f.close()
