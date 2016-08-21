#!/usr/bin/env python
import sys, math
import itertools

def solve(lenth,output_num):
    candidate = [ '1{}1'.format(''.join(p)) for p in itertools.product('01', repeat=(lenth-2))]
    count = 0

    for i in candidate:
        divisor = []
        good = True

        for base in range(2,11):
            numbybase = powerbase(lenth, i , base)
            
         
            factor = find_factor(numbybase)
            if factor == 0:
                good = False
                break;
            else:
                divisor.append(factor)
        if good:

            print '%s %s' % (i, ' '.join(map(str, divisor)))

            count += 1
            if count == output_num:
                return
def powerbase(lenth,str1,base):
    value = 0

    for t in xrange(lenth):


        value = value + int(str1[lenth-t-1])*(base**t)
    return value

def find_factor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

def main():
    with open(sys.argv[1]) as f:
        case_num = int(f.readline())

        for t in xrange(case_num):
            case = f.readline().strip()
            case_info = case.split()
           

            lenth = int(case_info[0])
            output_num = int(case_info[1])
            print 'Case #1:'

            s = solve(lenth,output_num)

           


if __name__ == '__main__':
    main()
