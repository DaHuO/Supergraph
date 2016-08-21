t = int(raw_input())  # read a line with a single integer

def flip(stack,x): #flips all x elements from the top of the stack)
    for i in range(0,len(stack[:x])):
        if stack[i] == '+':
                stack[i] = '-'
        else:
                stack[i] = '+'
    return stack

#----------------------------------------------------------------------

for i in xrange(1, t + 1):
    s = raw_input()  #read string of pancakes, yum yum :
    steps = 0
    stack = [j for j in s]
    
    for n in range (1,len(stack)+1):
        if stack[-n] == '-':
            #print "checking if pancake",n,"from the bottom is blank"
            flip(stack,len(stack)+1-n)
            #print "The stack has been flipped:",stack 
            steps += 1
    print "Case #{}: {}".format(i, steps)