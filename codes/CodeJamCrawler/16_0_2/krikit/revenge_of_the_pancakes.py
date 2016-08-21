#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
Google CodeJam 2016 qualification round B Revenge of the Pancakes
__author__ = 'krikit (krikit@naver.com)'
__copyright__ = 'Copyright (C) 2016-, No right reserved. ;)'
"""


###########
# imports #
###########
import argparse
import sys


#############
# functions #
#############
def solve(pancakes):
    """
    solve the problem
    :param  pancakes:  pancakes
    :return:           result
    """
    num_flip = 0
    for i in xrange(len(pancakes)-1):
        num_flip += 1 if pancakes[i] != pancakes[i+1] else 0
    return num_flip + (1 if pancakes[-1] == '-' else 0)


########
# main #
########
def main(fin, fout):
    """
    Revenge of the Pancakes
    :param  fin:   input file
    :param  fout:  output file
    """
    num_cases = int(fin.readline().strip())
    for case in xrange(1, num_cases+1):
        pancakes = fin.readline().strip()
        print >> fout, 'Case #%d: %d' % (case, solve(pancakes))


if __name__ == '__main__':
    _PARSER = argparse.ArgumentParser(description='Revenge of the Pancakes')
    _PARSER.add_argument('--input', help='input file <default: stdin>', metavar='FILE',
                         type=file, default=sys.stdin)
    _PARSER.add_argument('--output', help='output file <default: stdout>', metavar='FILE',
                         type=argparse.FileType('w'), default=sys.stdout)
    _ARGS = _PARSER.parse_args()
    main(_ARGS.input, _ARGS.output)
