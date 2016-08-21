#!/usr/bin/python

import sys

def get_flips(stack):
    #print('-'*10)
    #print(stack)
    count = 0
    while '-' in stack:
        start = stack[0]
        for i in range(1,len(stack)+1):
            if stack[i] != start:
                #print('Flipping at i = {:}'.format(i))
                stack = flip(i, stack)
                #print(stack)
                count += 1
                break
                
            #thisNum = stack[:i].count('+') - stack[:i].count('-')
            #print('i=  {:}, thisNum = {:}'.format(i, thisNum))
            #if thisNum < maxNum:
            #    maxNum = thisNum
            #    ind = i
        #count += 1
        #if tstack != stack:
        #    stack = tstack
        #    print(stack)
        #else:
        #    print(stack)
        #    sys.exit(0)

        #if '-' not in stack:
        #    return count
    return count

def flip(ind, stack):
    #print('FLIP IT')
    stack = list(stack)
    thisStack = list(stack[0:ind])
    thisStack.reverse()
    #print("reversed")
    #print(thisStack)
    for i in range(ind):
        if thisStack[i] == '-':
            thisStack[i] = '+'
        else:
            thisStack[i] = '-'
    stack[0:ind] = thisStack
    return ''.join(stack)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        cases = int(f.readline())
        for case in range(cases):
            stack = f.readline()
            ans = get_flips(stack)
            print("Case #{:}: {:}".format(case+1, ans))


