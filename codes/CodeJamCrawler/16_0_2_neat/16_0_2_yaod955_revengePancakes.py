import sys

cases = []

def flip(stack,end):
    end[0]+=stack[0]
    stack.reverse()
    return stack[:-1]+end

def parseStack(s):
    count = True
    stack = [0]
    for c in reversed(s):
        if ((c == '+')==count):
            stack[-1] += 1
        else:
            count = not count
            stack.append(1)
    stack.reverse()
    return stack

with open(sys.argv[1]) as f:
    for i in range(1,int(f.readline())+1):
        num_flips = 0
        stack = parseStack(f.readline().strip())
        while(len(stack)>1):
            if(len(stack)%2==0):
                stack = flip(stack[:-1],stack[-1:])
            else:
                stack = flip(stack[:-2],stack[-2:])
            num_flips += 1        
        s = 'Case #'+str(i)+': '+str(num_flips)+'\n'
        print(s)
        cases.append(s)

with open(sys.argv[2],'w+') as g:
    g.writelines(cases)
#             