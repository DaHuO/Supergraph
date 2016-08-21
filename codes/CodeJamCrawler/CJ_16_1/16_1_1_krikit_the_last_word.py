#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
Google CodeJam 2016 round 1A The Last Word
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
def solve(word):
    """
    solve the problem
    :param  word:  given word
    :return:       the last word
    """
    last_word = [word[0], ]
    for char in word[1:]:
        if char >= last_word[0]:
            last_word.insert(0, char)
        else:
            last_word.append(char)
    return ''.join(last_word)


########
# main #
########
def main(fin, fout):
    """
    Counting Sheep
    :param  fin:   input file
    :param  fout:  output file
    """
    num_cases = int(fin.readline().strip())
    for case in xrange(1, num_cases+1):
        word = fin.readline().strip()
        print >> fout, 'Case #%d: %s' % (case, solve(word))


if __name__ == '__main__':
    _PARSER = argparse.ArgumentParser(description='Counting Sheep')
    _PARSER.add_argument('--input', help='input file <default: stdin>', metavar='FILE',
                         type=file, default=sys.stdin)
    _PARSER.add_argument('--output', help='output file <default: stdout>', metavar='FILE',
                         type=argparse.FileType('w'), default=sys.stdout)
    _ARGS = _PARSER.parse_args()
    main(_ARGS.input, _ARGS.output)
