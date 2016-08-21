#!/usr/bin/env python

IN='./B-large.in'
OUT='./B-large.out'


def get_result(test):
    test = sorted(test)
    row = []
    for l in test:
        l  = l.split()
        row += l
    result = []
    pre = None
    count = {}
    for i in sorted(row):
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] +1

    for i in count:
        if count[i] % 2 == 1:
            result.append(i)
    return ' '.join(map(str, sorted(map(int,result))))

def testcase():
    test = []
    with open(IN, 'r') as inf:
        num = inf.readline()
        i = 0
        while i < int(num):
            i += 1
            case = []
            nc =  inf.readline()
            j = 0 
            while j < 2 * int(nc) - 1:
                j += 1
                case.append(inf.readline().strip())
            test.append(case)
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
