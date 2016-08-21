#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys


# use with
# python pancake.py < sample.in > sample.res 2> sample_dbg.res 1>&2; vim sample.in sample.res sample_dbg.res
# python pancake.py < A-small-attempt0.in > A-small-attempt0.res; vim A-small-attempt0.res A-small-attempt0.in
# python pancake.py < B-small-attempt0.in > B-small-attempt0.res 2> sample_dbg.res 1>&2; vim B-small-attempt0.res B-small-attempt0.in


debug_lvl = logging.DEBUG
def set_logging():
    log = logging.Logger("debug_logger")
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(filename)s - %(message)s')

    # STREAM CHANNEL - STDERR
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(debug_lvl)
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log

logger = set_logging()

def test_list(pan_list):
    logger.debug("test: list: %s" % (str(pan_list)))
    for pan in pan_list:
        if not pan:
            return False
    return True

def first_opposite(pan_list):
    polarity = pan_list[0]
    logger.debug("first 1: list: %s, len: %d, polarity: %s" % (str(pan_list), len(pan_list), str(polarity)))
    if len(pan_list)>1:
        logger.debug("first 2")
        for pan_index in range(1, len(pan_list)):
            logger.debug("first 3")
            if pan_list[pan_index] != polarity:
                logger.debug("first 4")
                logger.debug("return %d" % (pan_index-1))
                return pan_index-1
        logger.debug("return %d" % (len(pan_list)-1))
        return len(pan_list)-1
    logger.debug("return %d" % (0))
    return 0

def do_it(pan_list, number):
    new_pan_list=pan_list
    logger.debug("do_it 1: num:%d, before: %s  after %s" % (number, str(pan_list), str(new_pan_list)))
    for pan_index in range(0, number+1):
        logger.debug("do_it 2")
        if pan_list[pan_index]:
            logger.debug("do_it 3")
            new_pan_list[pan_index]=False
        else:
            logger.debug("do_it 4")
            new_pan_list[pan_index]=True
    logger.debug("do_it 5: before: %s  after %s" % (str(pan_list), str(new_pan_list)))
    return new_pan_list

def how_to_flip(iter, list_of_pan):
    return first_opposite(list_of_pan) # Strategy

def flip(initial_list, iteration, number):
    logger.debug("flip: list: %s, iteration: %d, number: %d" % (str(initial_list), iteration, number))
    new_list=do_it(initial_list, number)
    if test_list(new_list):
        return iteration # finished
    else:
        num = how_to_flip(iteration+1, new_list)
        return flip(new_list,iteration+1, num)

def solve(logger, nbr, new_list_of_pan):
    if test_list(new_list_of_pan):
        return 0
    else:
        return flip(new_list_of_pan, 1, how_to_flip(1,new_list_of_pan))

def transform(list_of_pan):
    new_list_of_pan=[]
    for pan in list_of_pan:
        if pan == "+":
            new_list_of_pan.append(True)
        else:
            new_list_of_pan.append(False)
    return new_list_of_pan

def main():
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        list_of_pan = list(raw_input())
        new_list_of_pan = transform(list_of_pan)
        logger.debug("--------")
        logger.debug("   list: %s" % str(list_of_pan))
        logger.debug("newlist: %s" % str(new_list_of_pan))
        print("Case #%i: %s" % (caseNr, solve(logger, caseNr, new_list_of_pan)))


if __name__ == "__main__":
    main()
