#!/usr/bin/env python

IN='./C-large.in'
OUT='./C-large.out'

def testcase():
    test = []
    with open(IN, 'r') as inf:
        num = inf.readline()
        for line in inf:
            test.append(line.strip())
    return test

def get_result(test):
    digit, case = test.split()
    digit = int(digit)
    case = int(case)
    start = init_v(digit)
    result = []
    while len(result) < case:
        if not start:
            break
        check(result, start)
        start = increase(start)
    return '\n' + '\n'.join(result)

def check(result, start):
    r = [start, ]
    for b in range(2,11):
        val = int(start, base=b)
        dvs = get_dvs(val)
        if not dvs:
            return
        r.append(str(dvs))
    result.append(' '.join(r))
        
def get_dvs(val):
    i = 2
    while i < val:
        if val % i == 0:
            return i
        i += 1
        if i > 500000:
            return None
    return None
            

def init_v(digit):
    result = '0' * (digit - 2)
    return '1' + result + '1'   

def increase(num):
    val = num[1:-1]
    valid = False
    for i in val:
        if i == '0':
            valid = True
            break
    if not valid:
        return None
    b10 = int(val, base=2) + 1
    return '1' + tob2(b10).zfill(len(num) -2) + '1'

def tob2(b10):
    result = ''
    while b10 > 0:
        result = str(b10 % 2) + result
        b10 = b10 / 2
    return result

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
