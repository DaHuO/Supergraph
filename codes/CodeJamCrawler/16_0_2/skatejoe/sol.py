import sys

def flip(stack,n):
    stack = list(reversed(stack[:n])) + stack[n:]
    for i in range(n):
        stack[i] = '-' if stack[i]=='+' else '+'
    return stack


def solve(stack):
    n = 0
    while '-' in stack:
        if stack[0] ==  '-':
            for i,char in enumerate(stack):
                if char=='+':
                    i-=1
                    break
            stack = flip(stack,max(1,i+1))
        elif stack[0] ==  '+':
            for i,char in enumerate(stack):
                if char=='-':
                    break
            stack = flip(stack,max(1,i))
        n+=1

    return n

with open(sys.argv[1],'r') as f:
    testcases = int(f.readline())
    for t in range(1,testcases+1):
        line = f.readline()[:-1]
        #print('test: ',line)
        print('Case #%d: %s' % (t,solve(list(line))))
