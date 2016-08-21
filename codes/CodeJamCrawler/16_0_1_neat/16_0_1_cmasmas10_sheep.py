import numpy as np
import sys

def check_digits(N):
    digits = {'0','1','2','3','4','5','6','7','8','9'}

    current_N = N
    while True:
        stringified_num = str(current_N)
        for digit in stringified_num:
            try:
                digits.remove(digit)
            except:
                pass

        #All digits found
        if not digits:
            return current_N
        #Overflow
        if sys.maxint-current_N <= N:
            return 'INSOMNIA'
        #Next number
        previous_N = current_N
        current_N += N
        if previous_N == current_N:
            return 'INSOMNIA'

    print N

if __name__ == "__main__":

    T = int(sys.stdin.readline()) #number of test cases

    for i in xrange(1,T+1):
        N = int(sys.stdin.readline())
        print 'Case #%d: %s' %(i,check_digits(N))



