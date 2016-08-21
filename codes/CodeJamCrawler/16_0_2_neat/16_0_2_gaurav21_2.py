#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cont_saxena
#
# Created:     08/04/2016
# Copyright:   (c) cont_saxena 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def minimizeStack(S):
    newStack = []
    last = None
    for i in range(len(S)):
        if(last != S[i]):
            newStack.append(S[i])
            last = S[i]
    return newStack

def Solve(N):
    stack = [ x for x in N ]
    num = 0
    test = 0
    if len(stack) == 1:
        if(stack[0]=='+'):
            return 0
        else :
            return 1
    if list(set(stack)) == ['+']:
        return 0
    if list(set(stack)) == ['-']:
        return 1
    #print stack
    stack = minimizeStack(stack)
    #print stack
    num = len(stack)
    num = num -1 if stack[-1] == '+' else num

    return num

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        N = f.readline()
        num = Solve(N.rstrip('\n'))
        print ("Case #"+str(case)+": "+str(num))