#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys

debug_lvl = logging.DEBUG
# debug_lvl = logging.INFO


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

def get_digits(logger, value):

    div=10000 # min case 0-200
    #div=1 000 000 # max case 0-10^6

    value = int(value)
    logger.debug("value:%d" % (value))
    tmp_value = value

    digit_list=[]
    process = False
    while ((tmp_value>=0) and (div!=0)):
        digit = tmp_value/div
        digit_r = tmp_value%div
        logger.debug("tmp_value:%d div:%d digit:%d digit_r:%d" % (tmp_value, div, digit, digit_r))

        if ((digit == 0 and (len(digit_list)!=0)) or # give zeros when in the middle
           (tmp_value >= div) or # checking that div wil not give upper zero
           (tmp_value==0 and div==1)): # give last zero # todo verify
            process = True
        else:
            div/=10
            process = False

        if process:
            if (digit<10):
                process = True
            else:
                div*=10
                process = False

        if process:
            tmp_value = tmp_value - (digit*div)
            div/=10
            digit_list.append(digit)

    logger.debug("digit list for %d: %s" % (value, str(digit_list)))
    return digit_list

def solve(logger, nbr, cipher):
    """
    """
    nbr=int(cipher[0])
    digits_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    MAX=1000000
    for N in range(1, MAX):
        if (N == MAX-1) or (nbr ==0):
            return "INSOMNIA"
        current_value = N*nbr
        digit_list=get_digits(logger, current_value)
        for i in digit_list:
            digits_dict[i]=1
            logger.debug("dict:%s" % (str(digits_dict)))

        if (digits_dict[0] and digits_dict[1] and digits_dict[2] and
            digits_dict[3] and digits_dict[4] and digits_dict[5] and
            digits_dict[6] and digits_dict[7] and digits_dict[8] and
            digits_dict[9]):
            break;
    return current_value

def main():
    logger = set_logging()

    testcases = input() # Get number of test cases
    for caseNr in xrange(1, testcases+1):
        cipher = []
        cipher.append(raw_input())
        print("Case #%i: %s" % (caseNr, solve(logger, caseNr, cipher)))


if __name__ == "__main__":
    main()
