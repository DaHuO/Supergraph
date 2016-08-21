
def flip(stack,index):
    aux = []
    for i in range(index + 1):
        aux.append( not stack.pop(0))

    for b in aux:
        stack.insert(0,b)

def ishappy(stack):
    for b in stack:
        if not b:
            return False
    return True

infile = open('input.in','r')
outfile = open('output.out','w')
T=int(infile.readline())

for t in range(T):
    pancakes = infile.readline()

    stack = []

    for p in pancakes:
        if p == '+':
            stack.append(True)
        if p == '-':
            stack.append(False)
    ops = 0
    print(stack)
    for i in range(len(stack)-1,-1,-1):
       if not stack[i]:
           if stack[0]:
               index = 0
               while(stack[index]):
                   index+=1
               index-=1
               flip(stack,index)
               ops +=1
           flip(stack,i)
           ops+=1
    #print(stack)
    print(ops)
    outfile.write('Case #'+str(t+1)+": "+str(ops)+"\n")