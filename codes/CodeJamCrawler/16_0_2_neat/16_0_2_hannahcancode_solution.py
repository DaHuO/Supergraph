I = open('B-large.in', 'r')
O = open('output.txt', 'w')

cases = 0

def flip(stack):
    flippedstack = []
    for cake in stack[::-1]:
        if cake == '+':
            flippedstack.append('-')
        if cake == '-':
            flippedstack.append('+')
    return flippedstack

I.readline()

for line in I:
    cases += 1
    aim = '+'
    count = 0
    stack = list(line.rstrip('\n'))
    plus = 0
    minus = 0
    search = True
    #print cases
    #
    print stack
    tempstack = stack[::-1]
    #stack.reverse()
    for i, cake in reversed(list(enumerate(stack))):
        if search == True:
            print cake
            if cake == '+':
                stack.pop()
                print "initial "+str(cases),stack

            elif cake == '-':
                search == False
                break
        else: break
    
    for c in stack:
        if c == '+':
            plus += 1
        elif c == '-':
            minus += 1
    if minus > plus:
        aim = '-'

    while ('+' in stack) and ('-' in stack):
        tempstack = stack[::-1]
        for i, cake in enumerate(tempstack):
            
            if cake != aim:
                stack = flip(tempstack[i:])+tempstack[:i]
                print stack
                count += 1
                break
            
    if '-' in stack:
        stack = flip(stack)
        count += 1
    if '+' in stack:
        pass
    print cases, count, stack
    O.write("Case #"+str(cases)+": "+str(count)+"\n")