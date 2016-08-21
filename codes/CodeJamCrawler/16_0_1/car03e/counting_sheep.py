import argparse


def parse_args():
    """Parses the command line arguments and returns a dictionary of args and
    their values."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the file with all the input values")
    return parser.parse_args()

def sheep_generator(n):
    """ Sheep generator that starts from n sheep and generates (i + 1) * n
        sheep with each successive call. """
    assert n >= 0

    count = 1
    while True:
        yield n * count
        count += 1

def counting_sheep(n):
    """ Returns the last sheep number that will be named. This number completes
        the set of numbers seen from 0-9. """
    assert n >= 0

    if n == 0:
        return float( 'inf' )

    numbers = set()

    for sheep in sheep_generator(n):
        for digit in str( sheep ):
            numbers.add( digit )
        if len( numbers ) == 10:
            return sheep


def main():
    args = parse_args()
    incoming = args.input
    outgoing = incoming.replace( ".in", ".out" )

    with open( incoming, "r" ) as f:
        trials = int( f.readline().strip() )

        for i in range( 1, trials + 1 ):
            n = int( f.readline().strip() )
            sheep = counting_sheep(n)

            if sheep == float( "inf" ):
                result = "Case #{}: {}".format( i, "INSOMNIA" )
            else:
                result = "Case #{}: {}".format( i, sheep )

            with open( outgoing, "a" ) as o:
                o.write( result )
                if i < trials:
                    o.write( "\n" )


if __name__ == "__main__":
    main()


def test_counting_sheep_infinity():
    n = 0
    assert counting_sheep(n) == float( 'inf' )

def test_counting_sheep_one():
    n = 1
    assert counting_sheep(n) == 10

def test_counting_sheep_two():
    n = 2
    assert counting_sheep(n) == 90

def test_counting_sheep_three():
    n = 11
    assert counting_sheep(n) == 110

def test_counting_sheep_four():
    n = 1692
    assert counting_sheep(n) == 5076
