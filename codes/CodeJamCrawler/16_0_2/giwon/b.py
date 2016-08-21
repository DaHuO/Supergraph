#!/usr/bin/env python


import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S')
logger = logging.getLogger( 'main' )


def get_minimum_flip_count( pancakes, target ):
    cnt = len(pancakes)
    if cnt == 0:
        return 0

    last_pancake = pancakes[cnt-1]
    if last_pancake == target:
        return get_minimum_flip_count( pancakes[:cnt-1], last_pancake )
    else:
        return get_minimum_flip_count( pancakes[:cnt-1], last_pancake ) + 1

def get_optimal_flip_count( line ):
    line = line.strip()
    fields = line.split( ' ' )
    pancakes = fields[0]

    cnt = len(pancakes)
    last_pancake = pancakes[cnt-1]

    n = get_minimum_flip_count( pancakes[:cnt-1], last_pancake )
    if last_pancake == '-':
        n = n + 1
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
        res = get_optimal_flip_count( lines[idx] )
        logger.info( "Case #%d: %d", test, res )
        file_out.write( "Case #{0}: {1}\n".format(test, res) )
        idx += 1

    file_out.close()
