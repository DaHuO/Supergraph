import random
import math

outf = open( 'out.txt', 'w' )

J = 16
N = 50

coins = []
while( len( coins ) < N ):
    num = bin( random.randrange( pow( 2, J - 2 ), pow( 2, J - 1 ) ) )[2:] + '1'
    for i in range( 2, 11 ):
        n = int( num, i )
        if( pow( 2, n - 1, n ) % n == 1 ):
            break
    else:
        if( num not in coins ):
            coins.append( num )


factors = []
for coin in coins:
    f = []
    for i in range( 2, 11 ):
        n = int( coin, i )
        j = 2
        found = False
        while( j <= math.sqrt( n ) ):
            if( n % j == 0 ):
                found = True
                break
            j += 1
        if( not found ):
            print 'FUCK'
            print n, 'is prime'
        else:
            f.append( j )
    factors.append( f )

outf.write( 'Case #1:\n' )
for i in range( len( coins ) ):
    outf.write( str( coins[ i ] ) + ' ' + ' '.join( [ str( x ) for x in factors[ i ] ] ) + '\n' )
