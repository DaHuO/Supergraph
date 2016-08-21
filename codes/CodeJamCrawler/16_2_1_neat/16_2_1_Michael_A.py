import collections
import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer( base = 10 ):
    return int( read_line(), base )

def read_integers( base = 10 ):
    return [ int( x, base ) for x in read_line().split() ]

def read_float():
    return float( read_line() )

def read_floats():
    return [ float( x ) for x in read_line().split() ]

def read_string():
    return read_line().strip()

def read_strings():
    return read_line().split()

def input_string_stack():
    data = []
    for line in sys.stdin.readlines():
        data.extend( line.split() )
    data.reverse()
    return data

def input_integer_stack():
    return [ int( x ) for x in read_string_stack() ]

def bits( x ):
    return bin( x ).count( '1' )

class memoized( object ):
   def __init__( self, function ):
      self.function = function
      self.cache = {}
   def __call__( self, *arguments ):
      try:
         return self.cache[ arguments ]
      except KeyError:
         value = self.function( *arguments )
         self.cache[ arguments ] = value
         return value

def contains( count, index ):
    return all( count[ letter ] for letter in digits[ index ] )

def deduct( count, index ):
    for letter in digits[ index ]:
        count[ letter ] -= 1

def restore( count, index ):
    for letter in digits[ index ]:
        count[ letter ] += 1

def number( build, count, index ):
    #print ''.join( str(x) for x in build ), index, count
    if sum( count.itervalues() ) == 0:
        return build
    if contains( count, index ):
        deduct( count, index )
        build.append( index )
        if number( build, count, index ):
            return build
        build.pop()
        restore( count, index )
    if index < 9 and number( build, count, index + 1 ):
        return build

digits = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    S = read_string()
    count = collections.defaultdict( int )
    for letter in S:
        count[ letter ] += 1
    print ''.join( str( x ) for x in number( [], count, 0 ) )
