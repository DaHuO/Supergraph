'''
Created on Apr 9, 2016

@author: christoph
'''

def flip(stack, num):
    flip = ""
    for c in stack[0:num]:
        if c == "-":
            flip = "+" + flip
        else:
            flip = "-" + flip
    return flip + stack[num:]

def doIt(stack,depth):
    if not "-" in stack:
        return depth
    if stack.startswith("+"):
        return doIt(flip(stack,stack.find("-")), depth+1)
    else:
        return doIt(flip(stack, stack.rfind("-")+1), depth+1)
    

def main():  
    T = int(raw_input())
    for i in range(T):
        stack = raw_input()
        out = doIt(stack,0)
        print "Case #" + str(i+1) + ": " + str(out)


if __name__ == "__main__":
    main()