import argparse
import collections


def parse_args():
    """ Parses the command line arguments and returns a dictionary of args and
        their values. """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the file with all the input values")
    return parser.parse_args()

def find_missing_row_or_col( n, grid ):
    """ Returns the missing row or column of heights. """
    numbers = collections.defaultdict( int )

    for row in grid:
        for number in row:
            numbers[ number ] += 1

    result = []

    # since there should be 2N lists, each number should show up an even
    # number of times so capture the numbers that don't and those are the
    # missing values
    for num, freq in numbers.items():
        if freq % 2 == 1:
            result.append( num )

    assert len( result ) == n

    result.sort()
    return result


def main():
    args = parse_args()
    incoming = args.input
    outgoing = incoming.replace( ".in", ".out" )

    with open( incoming, "r" ) as f:
        trials = int( f.readline().strip() )

        for i in range( 1, trials + 1 ):
            n = int( f.readline().strip() )

            grid = []
            for j in range( 2 * n - 1 ):
                row = [ int( k ) for k in f.readline().strip().split() ]
                grid.append( row )

            missing = find_missing_row_or_col( n, grid )

            result = "Case #{}: {}".format(
                i, " ".join( str( p ) for p in missing )
            )

            with open( outgoing, "a" ) as o:
                o.write( result )
                o.write( "\n" )

if __name__ == "__main__":
    main()

def test_find_missing_row_or_col():
    grid = [ [ 1, 2, 3],
             [ 2, 3, 5],
             [ 3, 5, 6],
             [ 2, 3, 4],
             [ 1, 2, 3], ]

    assert find_missing_row_or_col( 3, grid ) == [ 3, 4, 6 ]
