t = int( raw_input() )

def solve( N ):
    d = set()
    S = set( [ '0','1','2','3','4','5','6','7','8','9' ] )
    m = 1
    while True:
        p = m * N
        if p in d:
            return 'INSOMNIA'
        else:
            strings = str( p )
            for string in strings:
                S.discard( string )
            if not S:
                return p
            else:
                d.add( p )
        m += 1   

for i in xrange( t ):
    N = int( raw_input() )
    print "Case #%d: " % (i+1),solve( N )
