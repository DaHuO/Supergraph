inputs = int(raw_input())

def solve(pancakes):
    currStack = pancakes
    flips = 0

    while('-' in currStack):
        top = currStack[0]
        char = str()
        i = int()

        if(top == "+"):
            i = currStack.find("-")
            char = "-"
        elif(top == "-"):
            i = currStack.find("+")
            char = "+"

        if i == -1:
            i = len(currStack)
        currStack = (char * i) + currStack[i:]
        flips += 1

    return flips

for i in xrange(1, inputs + 1):
    print "Case #{}: {}".format(i, solve(raw_input()))
