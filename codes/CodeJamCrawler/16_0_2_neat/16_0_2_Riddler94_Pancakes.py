inp = open("B-large.in" , 'r')
out = open("B-large-out.txt", 'w')

def flipped(stack,pos):
    for j in xrange(len(stack[:pos+1])):
        if stack[j]=='-':
            stack[j]='+'
        else:
            stack[j]='-'
    stack[:pos+1] = stack[pos::-1]

def flip(stack):
    for j in xrange(len(stack)):
        if stack[j]=='-':
            stack[j]='+'
        else:
            stack[j]='-'
    stack = stack[::-1]

for case in xrange(int(inp.next())):
    stack = list(inp.next())
    del stack[-1]
    flips = 0
    for i in xrange(len(stack)-1):

        if(stack[i] == stack[i+1]):
            continue
        else:
            flipped(stack,i)
            flips += 1 
    if('-' in stack):
        flip(stack)
        flips += 1
    out.write("Case #%d: %d\n" % (case+1,flips))

inp.close()
out.close()
