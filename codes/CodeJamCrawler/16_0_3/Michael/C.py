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

primes = [ 3, 5, 7]

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 )
    N, J = read_integers()
    trial = 2**( N - 1 ) + 1
    while J:
        binary = bin( trial )[ 2 : ]
        divisors = []
        for base in range( 2, 11 ):
            number = int( binary, base )
            divisor = None
            root = int( number**0.5 )
            for prime in primes:
                if not number % prime:
                    divisor = prime
                    break
            if divisor:
                divisors.append( divisor )
            else:
                break
        else:
            print binary, ' '.join( str( divisor ) for divisor in divisors )
            J -= 1
        trial += 2
