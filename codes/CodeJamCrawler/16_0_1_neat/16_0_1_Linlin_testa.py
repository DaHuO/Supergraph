#!/usr/bin/env python

IN='./A-large.in'
OUT='./A-large.out'

def testcase():
    test = []
    with open(IN, 'r') as inf:
        num = inf.readline()
        for line in inf:
            test.append(line.strip())
    return test

def get_result(test):
    n = int(test)
    digit = get_digit(n)
    if len(digit) == 10:
        return str(n)
    i = 2
    while True:
        result = n * i
        if result == n:
            return 'INSOMNIA'
        digit = digit.union(get_digit(result))
        if len(digit) == 10:
            return str(result)
        i += 1 
def get_digit(i):
    digit = set()
    for d in str(i):
        digit.add(d)
    return digit

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
