import collections
import re
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

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    C, J = read_strings()
    length = len( C )
    format = '%0' + str( length ) + 'i'
    C = ( '00' + C.replace( '?', '.' ) )[ -length : ]
    J = ( '00' + J.replace( '?', '.' ) )[ -length : ]
    C_try = [ x for x in range( 10**length ) if re.match( C, format % x ) ]
    J_try = [ x for x in range( 10**length ) if re.match( J, format % x ) ]
    best = (10**20,0,0)
    for c in C_try:
        for j in J_try:
            test = abs( c - j ), c, j
            best = min( best, test )
    print format % best[ 1 ], format % best[ 2 ]
