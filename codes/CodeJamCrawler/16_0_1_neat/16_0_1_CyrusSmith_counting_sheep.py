#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from collections import Counter

if __name__ == '__main__':

    # Arguments parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', metavar='INFILE', 
                        type=argparse.FileType('r', 0), default='-',
                        help='input file')
    parser.add_argument('-o', '--output_file', metavar='OUTFILE', 
                        type=argparse.FileType('w', 0), default='-',
                        help='ouput file')
    args = parser.parse_args()

    to_find = frozenset(('1','2','3','4','5','6','7','8','9','0'))

    # Input file parsing
    case_max_num = int(args.input_file.readline().strip())
    case_num = 0

    for l in [l.strip() for l in args.input_file if l.strip()]:
        case_num += 1
        digits_found = set()
        number = int(l)
        if number == 0:
            args.output_file.write("Case #{0}: INSOMNIA\n".format(case_num))
        else:
            sum_num = number
            uniq_digits = list(Counter(list(str(sum_num))))
            digits_found |= set(uniq_digits)
            while digits_found != to_find:
                sum_num += number
                uniq_digits = list(Counter(list(str(sum_num))))
                digits_found |= set(uniq_digits)
            args.output_file.write("Case #{0}: {1}\n".format(case_num, sum_num))