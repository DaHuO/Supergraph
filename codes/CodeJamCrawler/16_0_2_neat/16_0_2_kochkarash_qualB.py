import sys
fileinput = sys.stdin

#import StringIO
#fileinput = StringIO.StringIO(inputstr)

T=int(fileinput.readline().strip())
for t in range(T):
    stack=list(fileinput.readline().strip())
    stack = [True if s=='+' else False for s in stack]
    l=len(stack)
    mincount =0;
    while(True):
        if all(stack):
            print "Case #%s: %s" % (t+1, mincount)
            break
        for i in range(l):
            if i==l-1 or stack[i]!=stack[i+1]:
                break
        flipped = stack[:i+1]
        flipped.reverse()
        flipped = [not f for f in flipped]
        stack = flipped+stack[i+1:]
        mincount += 1;

            