#!/usr/bin/env python
import sys

def solve(start_num):
    num_mark = [0,0,0,0,0,0,0,0,0,0]
    count_num = 0
    n = 1
    if start_num == 0:
        return "INSOMNIA"
    else:
        while (num_mark != [1,1,1,1,1,1,1,1,1,1]):
            count_num = start_num * n
            num_list = str(count_num)
            for i in num_list:

                num_mark[int(i)-1] = 1
            n = n+1
        return count_num


def process(f):
    case_num = int(f.readline())
    for t in xrange(case_num):
        start_num = int(f.readline())

        s = solve(start_num)

        print 'Case #%d: %s' % (t+1, s)


def main():
    with open(sys.argv[1]) as f:
        

        process(f)

if __name__ == '__main__':
    main()
