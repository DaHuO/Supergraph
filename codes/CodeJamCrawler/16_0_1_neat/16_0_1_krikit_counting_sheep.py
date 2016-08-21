#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
Google CodeJam 2016 qualification round A Counting Sheep
__author__ = 'krikit (krikit@naver.com)'
__copyright__ = 'Copyright (C) 2016-, No right reserved. ;)'
"""


###########
# imports #
###########
import argparse
import copy
import sys


#############
# constants #
#############
ALL = set([str(_) for _ in range(10)])


#############
# functions #
#############
def solve(start_str):
    """
    solve the problem
    :param  start_str:  start number string
    :return:            result string
    """
    start_num = int(start_str)
    num = start_num
    step = 0
    step_start_set = set(str(num))
    while True:
        if step_start_set == ALL:
            return str(num)
        step_acc_set = copy.deepcopy(step_start_set)
        for i in range(step+1, step+101):
            num = i * start_num
            step_acc_set.update(str(num))
            if step_acc_set == ALL:
                return str(num)
        if step_start_set == step_acc_set:
            return 'INSOMNIA'
        step += 100
        step_start_set = step_acc_set


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
        start = fin.readline().strip()
        print >> fout, 'Case #%d: %s' % (case, solve(start))


if __name__ == '__main__':
    _PARSER = argparse.ArgumentParser(description='Counting Sheep')
    _PARSER.add_argument('--input', help='input file <default: stdin>', metavar='FILE',
                         type=file, default=sys.stdin)
    _PARSER.add_argument('--output', help='output file <default: stdout>', metavar='FILE',
                         type=argparse.FileType('w'), default=sys.stdout)
    _ARGS = _PARSER.parse_args()
    main(_ARGS.input, _ARGS.output)
