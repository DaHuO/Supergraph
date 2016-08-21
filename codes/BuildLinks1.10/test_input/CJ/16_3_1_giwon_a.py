#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S')
logger = logging.getLogger( 'main' )


from heapq import *

def get_evacuation_plan( line1, line2 ):
    line1 = line1.strip()
    line2 = line2.strip()
    party_cnt = int(line1)
    parties = [int(n) for n in line2.split(' ')]
    rest = sum( parties )


    heap = []
    for party_idx, party_size in enumerate(parties):
        party_name = chr(ord('A') + party_idx)
        for i in xrange(1, party_size+1):
            heappush( heap, (i * -1, party_name) )

    res = []
    while True:
        try:
            party_rest, party_name = heappop( heap )
            rest = rest - 1
            if (len(heap) > 0) and (heap[0][0] * -2 > rest):
                party_rest2, party_name2 = heappop( heap )
                rest = rest - 1
                res.append( party_name + party_name2 )
            else:
                res.append( party_name )
        except IndexError:
            break

    return ' '.join(res)



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
        res = get_evacuation_plan( lines[idx], lines[idx+1] )
        logger.info( "Case #%d: %s", test, res )
        file_out.write( "Case #{0}: {1}\n".format(test, res) )
        idx += 2

    file_out.close()


# vim:ts=4:sw=4:expandtab:si
