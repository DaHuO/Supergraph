
inputFile = open( "B-large.in", "r" )
outputFile = open( "OUTPUT.txt", "w" )

def NOT(a):
    if a: return 0
    return 1

# repeat t times
for x in xrange( int(inputFile.readline().strip()) ):
    stack = []
    for s in inputFile.readline().strip():
        if s == "+": stack.append( 1 )
        else: stack.append( 0 )

    flips = 0
    while True:

        if sum(stack) == len(stack) or sum(stack) == 0:
            flips += NOT(stack[0])
            break

        first = stack[0]
        for i in xrange( 1, len(stack) ):
            if first != stack[i]: break

        stack = [ NOT(first) for pancakes in xrange(i) ] + stack[i:]
        flips += 1

    outputFile.write( "Case #%d: %d\n" %(x+1, flips) )

outputFile.close()