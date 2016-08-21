#!/usr/bin/env python


import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S')
logger = logging.getLogger( 'main' )


def get_digits( number ):
    digits = set()
    r = number % 10
    digits.add( r )
    number = number / 10
    while number > 0:
        r = number % 10
        digits.add( r )
        number = number / 10
    return digits

def get_last_number( line ):
    line = line.strip()
    fields = line.split( ' ' )
    initial_number = int(fields[0])

    if initial_number == 0:
        return 'INSOMNIA'

    n = initial_number
    digits = get_digits( n )
    while len(digits) < 10:
        logger.info( '%s %s', n, digits )
        n += initial_number
        digits = digits | get_digits( n )

    logger.info( 'DONE: %s %s', n, digits )
    return n


import sys

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    file_in = open( filename_in, 'r' )
    lines = file_in.readlines()
    file_in.close()

    testcnt = int(lines[0])
    file_out = open( filename_out, 'w' )

    idx = 1
    for test in range( 1, testcnt + 1 ):
        logger.info( "Case #%d", test )
        res = get_last_number( lines[idx] )
        file_out.write( "Case #{0}: {1}\n".format(test, res) )
        idx += 1

    file_out.close()
