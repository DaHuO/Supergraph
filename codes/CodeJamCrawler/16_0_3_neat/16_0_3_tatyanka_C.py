#!/usr/bin/python

import sys
import math


def is_prime(val):
    for i in xrange(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return i
    return None

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for i in xrange(t):
        line = sys.stdin.readline()
        parts = line.split()
        n = int(parts[0])
        j = int(parts[1])
        res_count = 0
        cur_try = 0
        print "Case #" + str(i + 1) + ":"
        while res_count < j:
            cur_bin = bin(cur_try)[2:]
            cur_str = '1' + '0' * (n - len(cur_bin) - 2) + cur_bin + '1'
            good = True
            current_num = cur_str
            #current_bases = cur_str
            for base in xrange(2, 11):
                if good:
                    #print "CUR_STR:", cur_str
                    cur_base_num = int(cur_str, base)
                    r = is_prime(cur_base_num)
                    if r == None or r == cur_base_num:
                        good = False
                    else:
                        current_num += ' ' + str(r)
                        #current_bases += ' ' + str(cur_base_num)
            if good:
                print current_num
                #print current_bases
                res_count += 1
            cur_try += 1    
