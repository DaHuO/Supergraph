inputFile = open( "INPUT.in", "r" )
outputFile = open( "OUTPUT.txt", "w" )

def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or \
    (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def prime(number):
    _prime = True
    for n in range( 2 , int(number**0.5)+1 ):
        if number % n == 0:
            _prime = False
            break
    return [ _prime, n ]

t = int( inputFile.readline().strip() )
( n, j ) = ( int(x) for x in inputFile.readline().strip().split() )
outputFile.write( "Case #1:\n" )

limit = int("1"*n,2) # limits to numbers of base 2 length n
jam = int("1"+"0"*(n-1),2)
count = 0

while jam <= limit and count < j:
    jamcoin = baseN( jam, 2 )

    # check that it starts and ends with 1's
    if jamcoin[0] != '1' or jamcoin[-1] != '1':
        jam += 1
        continue

    # check that only 1's and 0's appear
    brk = False
    for digit in xrange(2,10):
        if str(digit) in jamcoin:
            brk = True
            break
    if brk:
        jam += 1
        continue

    # check that base interpretations are not prime
    brk = False
    jamcoin = [ jamcoin ]
    for base in xrange( 2, 11 ):
        check = prime( int( jamcoin[0], base ) )
        if check[0]:
            brk = True
            break
        jamcoin.append( check[1] )

    if brk:
        jam += 1
        continue

    for i in xrange(9):
        outputFile.write( str(jamcoin[i]) + " " )
    outputFile.write( str(jamcoin[-1]) + "\n" )

    count += 1
    jam += 1
    print "Found %d jamcoins!" %(count)

outputFile.close()