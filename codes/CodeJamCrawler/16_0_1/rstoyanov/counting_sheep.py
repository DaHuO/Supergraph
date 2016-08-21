#!/usr/bin/python
def output(i,o):
    print "Case #" + str(i) + ": " + str(o)

def read_num(num):
    for i in xrange(len(str(num))):
        p = num % 10
        num /= 10
        check_table[int(p)] = 1

def is_it_time_to_sleep():
    for i in xrange(10):
        if check_table[i] == 0:
            return 0
    return 1

T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    check_table = [0] * 10
    fl = 0
    k = 1
    if N == 0:
        fl = 1
        output(i+1,"INSOMNIA")
        
    while fl == 0:
        read_num(k*N)
        fl = is_it_time_to_sleep()
        if fl == 1:
            output(i+1,k*N)
            break
        k += 1
