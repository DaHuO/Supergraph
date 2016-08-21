T = int( input() )
for Ti in range( 1, T+1 ):
    stack = input()
    prev = stack[0]
    moves = 0
    for cur in stack:
        if cur == prev:
            continue
        moves += 1
        prev = cur
        
    if prev == "-":
        moves += 1
    
    print( "Case #{0}: {1}".format( Ti, moves ) )