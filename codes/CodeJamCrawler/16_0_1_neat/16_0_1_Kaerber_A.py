def digits(n):
    return set( int(ch) for ch in n )
    
T = int( input() )
for Ti in range( 1, T+1 ):
    N = int( input() )
    
    result = "INSOMNIA"
    target = set( range( 10 ) )
    if N != 0:
        Nc = N
        while target:
            result = Nc
            target -= digits( str(Nc) )
            Nc += N
    print( "Case #{0}: {1}".format( Ti, result ) )