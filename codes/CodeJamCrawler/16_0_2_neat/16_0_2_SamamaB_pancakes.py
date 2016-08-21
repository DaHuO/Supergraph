def panCakes(stack):
    iterations = 0
    while(happyTest(stack) != True):
        if(unHappyTest(stack) == True):
            stack = flipAll(stack)
            iterations += 1
            return iterations

        pivot = 0
        for x in range(0, stack.__len__()-1):
            if(stack[x] != stack[x+1]):
                pivot = x
                break

        stack = flip(stack,pivot)
        iterations += 1
    return iterations

def happyTest(stack):
    size = 0
    for x in range(0, stack.__len__()-1):
        if(stack[x] == "+"):
            size += 1

    if(stack[stack.__len__()-1] != "\n"):
        if(size == stack.__len__()):
            return True
        else:
            return False

    elif(stack[stack.__len__()-1] == "\n"):
        if(size == stack.__len__()-1):
            return True
        else:
            return False

def unHappyTest(stack):
    size = 0
    for x in range(0, stack.__len__()-1):
        if(stack[x] == "-"):
            size += 1

    if(stack[stack.__len__()-1] != "\n"):
        if(size == stack.__len__()-1):
            return True
        else:
            return False

    elif(stack[stack.__len__()-1] == "\n"):
        if(size == stack.__len__()-1):
            return True
        else:
            return False

def flip(stack, pivot):
    if(stack[0] == "+"):
        stack = stack.replace("+", "-", pivot+1)

    else:
        stack = stack.replace("-", "+", pivot+1)
    return stack

def flipAll(stack):
    stack = stack.replace("-", "+")
    return stack

freader = open("B-large.in", "r")
fwriter = open("output.out", "w")
t = freader.readline()

for x in range(1, int(t)+1):
    t = freader.readline()
    fwriter.write("Case #{}: {}\n".format(x, panCakes(t)))

freader.close()
fwriter.close()