#!/usr/bin/python

def checkAll(dt):
    for i in range(10):
        if i not in dt:
            return False
    return True

def getCount(num):
    if num == 0:
        return -1
    dt = {}
    mult = 1
    found = True
    while True:
        tnum = num *mult
        inum = tnum
        found = False
        while True:
            d = tnum % 10
            tnum = tnum/10
            if d not in dt:
                found = True
                dt[d] = 1
            if tnum == 0:
                break

        if checkAll(dt):
                return inum
        mult += 1
        if mult > 10000000000:
            break
    return -1

f = open('A.small.txt', 'r')
tc = int(f.readline())
#print tc
for index in range(tc):
    num = int(f.readline())
    ct = getCount(num)
    if ct == -1:
        print "CASE #" + str(index+1) + ": INSOMNIA"
    else:
        print "CASE #" + str(index+1) + ": " +  str(ct)

'''
for line in f:
        print line
'''
