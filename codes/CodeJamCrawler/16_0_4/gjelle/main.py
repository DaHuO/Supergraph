#!/usr/bin/env python2.7

import sys


def challenge(k, c, s):
    """
    Produce set of tiles < s for finding gold in a fractal artwork of complexity c and originating from k tiles.
    :type k: int
    :type c: int
    :type s: int
    :rtype: list[int]
    """
    # A very simplified solution for "small dataset" where k = s.
    # We simply assign a student to look at each "leaf node tile". If any leaf contains gold, we are happy ;-)
    if s < k:
        return list()
    tile_width = k ** (c - 1)
    return [1 + (i * tile_width) for i in xrange(0, s)]


def main(stream):
    """
    :type stream: file
    """
    first_line = stream.readline()
    case_count = int(first_line)
    case_number = 1
    for line in stream:
        case_input = line.strip()
        input_list = case_input.split(None, 3)
        k = int(input_list[0])
        c = int(input_list[1])
        s = int(input_list[2])
        result = challenge(k, c, s)
        print 'Case #%(case_number)d: %(result)s' % dict(
            case_number=case_number,
            result=' '.join([str(tile) for tile in result]) or 'IMPOSSIBLE'
        )
        if case_number == case_count:
            break
        else:
            case_number += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        with open(file_name) as file_stream:
            main(file_stream)
    else:
        main(sys.stdin)
