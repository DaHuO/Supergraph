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

def missing( lines, rows, columns, trial_index ):
##    print
##    print lines
##    print rows
##    print columns

    if trial_index == len( lines ):
        return rows, columns
    for test_row in range( N ):
        if rows[ test_row ] is None:
            for index, item in enumerate( lines[ trial_index ] ):
                if columns[ index ] is not None and lines[ columns[ index ] ][ test_row ] != item:
                    break
            else:
                rows[ test_row ] = trial_index
                if missing( lines, rows, columns, trial_index + 1 ):
                    return rows, columns
                rows[ test_row ] = None
    for test_column in range( N ):
        if columns[ test_column ] is None:
            for index, item in enumerate( lines[ trial_index ] ):
                if rows[ index ] is not None and lines[ rows[ index ] ][ test_column ] != item:
                    break
            else:
                columns[ test_column ] = trial_index
                if missing( lines, rows, columns, trial_index + 1 ):
                    return rows, columns
                columns[ test_column ] = None

T = read_integer()
for t in range( T ):
    print 'Case #%i:' % ( t + 1 ),
    N = read_integer()
    lines = [ read_integers() for n in range( 2*N - 1 ) ]
    lines.sort()
    rows, columns = missing( lines, N*[ None ], N*[ None ], 0 )
    if None in rows:
        index = rows.index( None )
        line = [ lines[ column ][ index ] for column in columns ]
        rows[ index ] = 2*N - 1
    else:
        index = columns.index( None )
        line = [ lines[ row ][ index ] for row in rows ]
        columns[ index ] = 2*N - 1
    lines.append( line )
    assert line == sorted( line )
    assert len( set( rows ) ) == N
    assert len( set( columns ) ) == N
    assert len( set(rows).union( set( columns ) ) ) == 2*N
    assert sorted( set(rows).union( set( columns ) ) ) == range( 2*N )
    grid = [ lines[ row ] for row in rows ]
    for row in range( N ):
        assert grid[ row ] == sorted( grid[ row ] )
    for column in range( N ):
        line = [ grid[ row ][ column ] for row in range( N ) ]
        assert line == sorted( line )
        assert line == lines[ columns[ column ] ]
    print ' '.join( str( item ) for item in lines[ -1 ] )
