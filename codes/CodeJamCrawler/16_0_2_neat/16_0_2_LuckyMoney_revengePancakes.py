#!/usr/bin/env python
import sys

def solve(t, case_info,f):
    filp_time = f
    left_case = case_info

    n = len(left_case)


    chk, left_case = check(left_case)
    #import ipdb; ipdb.set_trace()
    if chk == 0:
        if left_case[n-1] == '+':
            back = countback(left_case)

            left_case = left_case[:(n-back)]

            solve(t, left_case,filp_time)    

        elif left_case[n-1] == '-':
            front,back = count(left_case)
            if front > back:
                left_case = flip(left_case)
                filp_time = filp_time+1

                solve(t,left_case,filp_time)
            else:
                
                left_case = left_case[:(n-back-1)]
                filp_time = filp_time+2
                solve(t, left_case,filp_time)
                
    elif chk == 1:
        print 'Case #%d: %s' % (t+1, filp_time)
        
        #return filp_time
    elif chk == 2:
        filp_time = filp_time + 1
        print 'Case #%d: %s' % (t+1, filp_time)
        #return filp_time + 1



def countback(case_info):
    back = 0
    reverse_case = case_info[::-1]
    for i in reverse_case:
        if i == '+':
            back = back+1
        else:
            return back

def check(case_info):
    n = len(case_info)
    a = n * '+'
    b = n * '-'

    if case_info == a:
        return 1, ''
    elif case_info == b:
        return 2, ''
    else:
        return 0, case_info

def count(case_info):
    front = 0
    back = 0

    for i in case_info:
        if i == '-':
            front = front+1
        else:
            break

    reverse_case = case_info[::-1]
    for i in reverse_case:
        if i == '-':
            back = back+1
        else:
            break

    return front, back    

def flip(case_info):
    after_filp = ''
    reverse_case = case_info[::-1]
    for i in reverse_case:
        if i == '+':
            after_filp = after_filp + '-'
        else:
            after_filp = after_filp + '+'
    return after_filp

def process(f):
    case_num = int(f.readline())
    for t in xrange(case_num):
        case_info = f.readline().strip()

        filp_time = 0

        s = solve(t, case_info, filp_time)

        #print 'Case #%d: %s' % (t+1, s)


def main():
    with open(sys.argv[1]) as f:
        

        process(f)

if __name__ == '__main__':
    main()
