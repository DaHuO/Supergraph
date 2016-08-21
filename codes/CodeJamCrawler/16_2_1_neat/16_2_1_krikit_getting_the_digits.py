#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
Google CodeJam 2016 round 1B Getting the Digits
__author__ = 'krikit (krikit@naver.com)'
__copyright__ = 'Copyright (C) 2016-, No right reserved. ;)'
"""


###########
# imports #
###########
import argparse
from collections import Counter
import sys


#############
# constants #
#############
_DIGITS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']


#############
# functions #
#############
def _is_in(to_find, where):
    """
    find count in other count
    :param  to_find:  count to find
    :param  where:    find in count
    :return:          whether in or not in
    """
    subtract = where - to_find
    return (subtract + to_find) == where


def _solve_inner(line_cnt, phone_number, try_num):
    """
    recursive try to find number using back tracking
    :param  line_cnt:      Counter object until this try
    :param  phone_number:  phone numbers until this try
    :param  try_num:       trial number
    :return:               phone numbers
    """
    if line_cnt == Counter():
        return phone_number
    for num, num_str in enumerate(_DIGITS):
        if num < try_num:
            continue
        digit_cnt = Counter(list(num_str))
        if _is_in(digit_cnt, line_cnt):
            phone_number.append(num)
            line_cnt -= digit_cnt
            return _solve_inner(line_cnt, phone_number, try_num)
    last_num = phone_number[-1]
    del phone_number[-1]
    digit_cnt = Counter(list(_DIGITS[last_num]))
    line_cnt += digit_cnt
    return _solve_inner(line_cnt, phone_number, last_num + 1)


def solve(line):
    """
    solve the problem
    :param  line:  line of string
    :return:       phone number
    """
    line_cnt = Counter(list(line))
    phone_number = []
    answer = _solve_inner(line_cnt, phone_number, 0)
    return ''.join([str(_) for _ in answer])


########
# main #
########
def main(fin, fout):
    """
    Getting the Digits
    :param  fin:   input file
    :param  fout:  output file
    """
    num_cases = int(fin.readline().strip())
    for case in xrange(1, num_cases+1):
        line = fin.readline().strip()
        print >> fout, 'Case #%d: %s' % (case, solve(line))


if __name__ == '__main__':
    _PARSER = argparse.ArgumentParser(description='The Last Word')
    _PARSER.add_argument('--input', help='input file <default: stdin>', metavar='FILE',
                         type=file, default=sys.stdin)
    _PARSER.add_argument('--output', help='output file <default: stdout>', metavar='FILE',
                         type=argparse.FileType('w'), default=sys.stdout)
    _ARGS = _PARSER.parse_args()
    main(_ARGS.input, _ARGS.output)
