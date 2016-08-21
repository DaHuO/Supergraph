#!/usr/bin/python -u
import itertools
from math import sqrt
import numpy

# Part of 2016 Google code jam

def find_number(s):
    num_list = []
    num_list[:0] = s
    num_list_save = list(num_list)
    final_pn = ''

    num_strs=['ZERO','TWO','FOUR','SIX','EIGHT','ONE','THREE','FIVE','SEVEN','NINE']
    dict = {'ZERO':'0','ONE':'1' ,'TWO':'2','THREE':'3','FOUR':'4' ,'FIVE':'5','SIX':'6','SEVEN':'7','EIGHT':'8','NINE':'9'}

    n = 0
    skip_num = -1

    found_letter=1

    while n < 10:
        if n == skip_num:
            n = n + 1
        else:
            num_letters = []
            num_letters[:0] = num_strs[n]

            for nl in num_letters:
                #print '   DEBUG ' + nl + ' in ' + str(num_list)
                if nl not in num_list:
                    #print '    DEBUG not in number'
                    found_letter = 0
                    break
                else:
                    #print '    DEBUG found letter'
                    num_list.remove(nl)

            if found_letter == 0:
                num_list = list(num_list_save)
                n = n + 1
                found_letter = 1
            else:
                num_list_save = list(num_list)
                final_pn = final_pn + dict[num_strs[n]]

        # edge case 
        if n == 10 and len(num_list) != 0 and skip_num < 10:
            skip_num = skip_num + 1
            #print '   DEBUG restarting for ' + final_pn + ' as ' + str(num_list) + ' is not empty (skip_num ' + str(skip_num) + ')'
            n = 0
            num_list = []
            num_list[:0] = s
            num_list_save = list(num_list)
            final_pn = ''

    final_pn = ''.join(sorted(final_pn))
    #print s + ' -> ' + final_pn
    return final_pn


T = int(raw_input().strip())

for i in range(1, T+1):
    s= raw_input().strip()
    print 'Case #' + str(i) + ': ' + find_number(s)
