#!/usr/bin/env python
import random

IN='./A-large.in'
OUT='./A-large.out'
num={0:'ZERO', 1:'ONE', 2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6: 'SIX',
    7:'SEVEN', 8:'EIGHT', 9:'NINE'}
N=[0,1,2,3,4,5,6,7,8,9]

def exist(tmp, s):
    for c in s:
        if c not in tmp:
            return False
        tmp.remove(c)
    return True

def guess(test, myN):
    result = ''
    for key in myN:
        s = num[key]
        while exist(test[:], s):
            for c in s:
                test.remove(c)
            result = result + str(key)
    return result, test
 

def get_result(test):
    test = sorted(test)
    result, left = guess(test[:], N)
    while left:
        tmp = N[:]
        random.shuffle(tmp)
        result, left  = guess(test[:], tmp)
    return ''.join(sorted(result))

def testcase():
    test = []
    with open(IN, 'r') as inf:
        num = inf.readline()
        for line in inf:
            test.append(line.strip())
    return test

def run():
    test = testcase()
    result = []
    for t in test:
       result.append(get_result(t)) 
    i = 1
    with open(OUT, 'w') as outf:
        for line in result:
            output = 'Case #%d: ' % i
            output = output + line
            print >> outf, output
            i += 1

if __name__ == '__main__':
    run()
