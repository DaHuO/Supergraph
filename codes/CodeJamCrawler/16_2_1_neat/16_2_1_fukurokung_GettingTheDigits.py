#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Problem A: Getting the Digits
#Author: Wongnaret Khantuwan

import itertools
result_set = itertools.permutations(["THREE", "SEVEN", "EIGHT", "NINE", "ZERO","FOUR", "FIVE", "ONE", "TWO",  "SIX"])
digit_dict = {"THREE":'3', "SEVEN":'7', "EIGHT":'8', "NINE":'9', "ZERO":'0',"FOUR":'4', "FIVE":'5', "ONE":'1', "TWO":'2', "SIX":'6'}
def allIn(text, keyword):
    #print 'test', keyword ,'in',text
    for tmp_char in keyword:
        if not tmp_char in text:
            return False

    if keyword == "THREE" or keyword == "SEVEN":
        return text.count('E')>=2
    elif keyword == "NINE":
        return text.count('N')>=2
    return True

def remove_keyword(text, keyword):
    for tmp_char in keyword:
        text = text.replace(tmp_char, '', 1)
    return text

def searchDigit(text, digit):
    #print 'search', digit, 'in', text
    result = ''
    while allIn(text, digit):
        result+=digit_dict[digit]
        text = remove_keyword(text, digit)
    return (result, text)

def getDigit(text):
    reset = text

    #print 'input:',text
    for digit in result_set:

        out = ''
        for i in range(0,10):
            (tmp, text) = searchDigit(text, digit[i])
            out += tmp


        if len(text)==0:
            #print 'remain:',text
            return out
        text = reset
    #print 'remain:',text
    return "ERROR"

#main function
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  input = raw_input()
  print "Case #%d: %s" % (i, ''.join(sorted(getDigit(input))))
