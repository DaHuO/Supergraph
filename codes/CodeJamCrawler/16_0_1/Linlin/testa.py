#!/usr/bin/env python

IN='./A-large.in'
OUT='./A-large.out'

def get_result(test):
    test = test.strip()
    result = test[0]
    for l in test[1:]:
        if l >= result[0]:
            result = l + result
        else:
            result = result + l
    return result

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
