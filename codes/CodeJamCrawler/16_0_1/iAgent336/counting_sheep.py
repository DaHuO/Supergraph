import numpy as np
import argparse

def solve(single_case):
    seen_digit = {}
    N = int(single_case)
    m = 1
    if(N==0): return 'INSOMNIA'        
    while(True):
        num_str = str(N*m)
        for c in num_str:
            #print c
            seen_digit[c] = True
        if(len(seen_digit.keys())==10): break
        else: m += 1
    return N*m

def main():
    testcases = input()
    for case_num in xrange(1, testcases+1):
        single_case = raw_input()
        print("Case #%i: %s" % (case_num, solve(single_case)))

def test():
    cipher = raw_input()
    print("Case #1: %s" % (solve(single_case)))


if __name__=='__main__':
    main()
    #test()


