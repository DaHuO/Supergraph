#!/usr/bin/python2.7

needed = [  str( x ) for x in range( 10 ) ]
def solve( N, mult=1 ):
    global needed
    prev = N
    temp = N * mult

    for eachDigit in str( temp ):
        if eachDigit in needed:
            needed.remove( eachDigit )

    if len( needed ) == 0:
        needed = [ str( x ) for x in range( 10 ) ]
        return str( temp )

    elif temp == prev and mult != 1:
        needed = [ str( x ) for x in range( 10 ) ]
        return "INSOMNIA"
    else:
        mult += 1
        return solve( N, mult )

out = open( 'output.txt', 'w' )
with open( 'input.txt', 'r' ) as f:
  cases = f.readline()
  case = 1
  for eachLine in f.readlines():
      if eachLine.strip() not in ['', None]:
          out.write( 'Case #' + str( case ) + ":  " )
          solution = solve( int( eachLine.strip() ) )
          solution = str( solve( int( eachLine.strip() ) ) ) + "\n"
          out.write( solution )
          case += 1
out.close()
