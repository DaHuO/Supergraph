#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:     sheep.py
Author:       neilhong
@date:        2016-04-09 09:48:36

Description:

Changelog:

'''

ALL_NUM = range(10)

def finish(r):
    return all(i in r for i in ALL_NUM)

def getNumbers(num):
    ret = set()
    step = 10
    while num > 0:
        tail = num % 10
        ret.add(tail)
        num = num / 10
    return ret

def check(num):
    if num == 0:
        return None
    i = 1
    cur_set = set()
    while True:
        last_val = num * i
        step_set = getNumbers(last_val)
        cur_set = cur_set.union(step_set)
        if finish(cur_set):
            return last_val
        i = i + 1
    return None

def run():
    f = open('A-large.in', 'r')
    f.readline()
    i = 0
    for case in f:
        i = i + 1
        ret = check(int(case))
        print 'Case #%s: %s' % (str(i), 'INSOMNIA' if ret is None else str(ret))

if __name__ == '__main__':
    #print getNumbers(101)
    #print getNumbers(123)
    #print getNumbers(89531)
    #print getNumbers(908811)
    run()
