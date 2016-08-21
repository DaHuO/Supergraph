#!/usr/bin/env python

IN='./B-small-attempt0.in'
OUT='./B-small-attempt0.out'

def testcase():
    test = []
    with open(IN, 'r') as inf:
        num = inf.readline()
        for line in inf:
            test.append(line.strip())
    return test

def get_result(test):
    num = 0
    tests = set()
    old = set()
    tests.add(test)
    old = old.union(tests)
    while not finish(tests):
        num += 1
        result = set()
        for t in tests:
            result = result.union(flip(t))
        tests = result - old
        old = old.union(tests)
    return str(num)
    
def flip(test):
    result = set()
    i = 1
    while i <= len(test):
        result.add(flip_top(test, i))
        i += 1
    return result    

def flip_top(p, num):
    top = p[0:num][::-1]
    newtop = ''
    for i in top:
        if i == '-':
            newtop += '+'
        else:
            newtop += '-'
    return newtop + p[num:]
        
def finish(li):
    for l in li:
        if is_done(l):
            return True
    return False

def is_done(p):
    for d in p:
        if d == '-':
            return False
    return True

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
