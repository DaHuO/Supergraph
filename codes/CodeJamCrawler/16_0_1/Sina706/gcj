#! /usr/bin/env python

import sys
def list_digits(n):
    digits=[]
    for d in str(n):
        if d not in digits:
            digits.append(d)
		 
    return digits

def count_itr(n):
    all_digits=[]
    n0=n
    nums=[]
    if n==0:
       return 'INSOMNIA'
    else:
        i=2
        while True:
            for d1 in list_digits(n):
                if d1 not in all_digits:
                    all_digits.append(d1)
            nums.append(n)
            n = n0*i
            i+=1
            if len(all_digits)==10:    
                return nums[-1] 

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        last_n=count_itr(n)
        print 'Case #{0}: {1}'.format(i, last_n)

if __name__=='__main__':
    main()
