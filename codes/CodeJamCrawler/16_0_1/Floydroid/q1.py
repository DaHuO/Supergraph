
inputFile = open( "A-large.in", "r" )
outputFile = open( "OUTPUT.txt", "w" )

t = int(inputFile.readline().strip())

# repeat t times
for x in xrange(t):

    n = int(inputFile.readline().strip())
    seen = [ 0 for i in xrange(10) ]

    i=0
    while sum(seen) < 10:
        i += 1
        nn = i * n
        for digit in str(nn):
            seen[ int(digit) ] = 1

        if i>1000:
            break

    if i > 1000:
        outputFile.write( "Case #%d: INSOMNIA\n" %(x+1) )
    else:
        outputFile.write( "Case #%d: %d\n" %(x+1, nn) )

outputFile.close()