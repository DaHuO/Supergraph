#!/usr/bin/env python
# vim: set fileencoding=utf-8
'''Module docstring
Template version: 1.2
'''

# for python2
from __future__ import division, print_function

import argparse
import sys
import os
import functools
import logging
# import heapq
# from operator import itemgetter
# from collections import defaultdict
# from collections import deque
# from array import array
# from bisect import bisect
# from math import sqrt

import string

VERSION = '%(prog)s 1.0'

# for interactive call: do not add multiple times the handler
if 'LOG' not in locals():
    LOG = None
LOG_LEVEL = logging.ERROR
FORMATER_STRING = ('%(asctime)s - %(filename)s:%(lineno)d - '
                   '%(levelname)s - %(message)s')


def configure_log(level=LOG_LEVEL, log_file=None):
    'Configure logger'
    if LOG:
        LOG.setLevel(level)
        return LOG
    log = logging.getLogger('%s log' % os.path.basename(__file__))
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stderr)
    log_formatter = logging.Formatter(FORMATER_STRING)
    handler.setFormatter(log_formatter)
    log.addHandler(handler)
    log.setLevel(level)
    return log

LOG = configure_log()


# pylint: disable=too-few-public-methods
class Memoized(object):
    '''Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


class CommentedFile(object):
    'Implements comments skip for file'
    def __init__(self, in_file, commentstring='#'):
        self.in_file = in_file
        self.commentstring = commentstring

    def next(self):
        'The next line but skips comments'
        line = self.in_file.next()
        while line.startswith(self.commentstring):
            line = self.in_file.next()
        return line

    def __iter__(self):
        return self
# pylint: enable=too-few-public-methods

def get_next_evacuates(current_senate):
    '''find 1 or 2 letters with max representative
    '''
    max_repr = max(current_senate.values())
    to_evacuate = []
    for letter, nb in current_senate.items():
        if nb == max_repr:
            # not most efficient as it can remove only 1 senator if its party
            # is single most represented
            to_evacuate.append(letter)
        if len(to_evacuate) >= 2:
            break
    return to_evacuate

def get_two_max_equal(current_senate):
    '''get the max to be shared with 2 senators
    and evacuate everybody else
    '''
    # find max and second max
    fst_max = None
    snd_max = None
    fst_letter = None
    snd_letter = None
    for letter, nb in current_senate.items():
        if fst_max is None or nb > fst_max:
            if fst_max is not None:
                # assign previous fst_max to snd
                snd_max = fst_max
                snd_letter = fst_letter
            fst_max = nb
            fst_letter = letter
            continue
        if snd_max is None or nb > snd_max:
            snd_max = nb
            snd_letter = letter
    LOG.debug('found 1st: ({}, {}), 2nd: ({}, {})'.format(fst_letter, fst_max,
                                                          snd_letter, snd_max))
    to_evacuate = []
    # make 2 max equal
    while current_senate[fst_letter] != current_senate[snd_letter]:
        to_evacuate.append(fst_letter)
        current_senate[fst_letter] -= 1
    # evacuate everybody else
    for letter, nb in current_senate.items():
        if letter == fst_letter or letter == snd_letter:
            continue
        doubles, singles = divmod(nb, 2)
        to_evacuate.extend(doubles * [2 * letter] + singles * [letter])
    # evacuate the 2 maxs
    rest = current_senate[fst_letter]
    assert current_senate[snd_letter] == rest
    to_evacuate.extend(rest * [fst_letter + snd_letter])
    return to_evacuate

def get_evacuation_plan(values):
    current_senate = dict(zip(string.ascii_uppercase, values))
    LOG.debug(current_senate)
    return get_two_max_equal(current_senate)

def do_job(in_file, out_file=sys.stdout):
    'Do the work'
    LOG.debug('Start working with files: %s and %s',
              in_file.name, out_file.name)
    # first line is number of test cases
    # pylint: disable=invalid-name
    T = int(in_file.readline())
    # pylint: enable=invalid-name
    for testcase in range(T):
        # pylint: disable=invalid-name
        N = int(in_file.readline())
        # pylint: enable=invalid-name
        # for integer input
        values = [int(x) for x in in_file.readline().split()]
        # for other inputs
#        values = in_file.readline().rstrip('\n')
        assert len(values) == N
        result = get_evacuation_plan(values)
        print_output(out_file, testcase, result)


def print_output(out_file, testcase, result):
    'Formats and print result'
    print('Case #%d:' % (testcase + 1), end=' ', file=out_file)
    print(' '.join(result), file=out_file)
    # print('%.6g' % result, file=out_file)


def create_parser():
    'Return the argument parser'
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help=argparse.SUPPRESS)
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-q', '--quiet', '--silent', dest='quiet',
                           action='store_true', default=False,
                           help='run as quiet mode')
    verbosity.add_argument('-v', '--verbose', dest='verbose',
                           action='store_true', default=False,
                           help='run as verbose mode')
    parser.add_argument('-t', dest='template', action='store_true',
                        default=False, help=('template name for construct'
                                             'out file name as in_file.out '
                                             '(default False)'))
    parser.add_argument('-w', dest='out_file',
                        help=('output file or stdout if FILE is - (default '
                              'case) or TEMPLATE.out (default if template is '
                              'given)'))
    # type=argparse.FileType('w')
    parser.add_argument('in_file', help='input file (default stdin)',
                        default=sys.stdin, type=argparse.FileType('r'))
    return parser


def main(argv=None):
    'Program wrapper'
    if argv is None:
        argv = sys.argv[1:]
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.INFO)
    if args.quiet:
        LOG.setLevel(logging.CRITICAL)
    if args.debug:
        LOG.setLevel(logging.DEBUG)
#    # unset verbose for easy option check
#    args.verbose = False
#    if not any(args.__dict__.values()):
#        parser.error('Must provide at least one option')
    if args.template and not args.out_file:
        args.out_file = ''.join((args.in_file.name, '.out'))
    if not args.out_file or args.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(args.out_file, 'w')
        except IOError:
            parser.error('Problem opening file: %s' % args.out_file)
    sys.setrecursionlimit(2**30-1)
    do_job(args.in_file, out_file)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
