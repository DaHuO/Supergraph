#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 00:38:49 2016

@author: jlindenger
"""

_MAX_TRIALS = 1000

def count_sheep(n):
    known_digits = []
    named_number = n    
    trial = 0

    while trial < _MAX_TRIALS:
        added_digit = False    
        for c in str(named_number):
            if c not in known_digits:
                known_digits.append(c)
                added_digit = True
                
        if len(known_digits) == 10:
            return str(named_number)
        
        if added_digit is False:
            trial += 1
        
        named_number += n
        
    return 'INSOMNIA'

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print('Case #%d: %s' % (i+1, count_sheep(n)))
        